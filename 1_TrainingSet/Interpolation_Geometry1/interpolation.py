import os
import numpy as np
from glob import iglob
import shutil
import os
import readline
import pprint
import sys
from sys import argv


'''This file should interpolate between a starting geometry taken from a QM.in file and an end-geometry (at which NNs broke down), also taken from a QM.in file_end
      - The files should be transfered into zmat-files and linear interpolation between the start- and end-geometry will be carried out
      - Later, the geometries will be written into the form of a QM.in file, the interface will then generate QM.out files - those will be written into an output.dat format and the output_all.dat can be appended later
      - In the end, the phases should be compared between geometries and corrected in the output.dat files. After the last geometry is corrected, the 
        calculation using a QM-interface, should be carried out with corrected phases
'''


#============================================================================================================================================================#
#================================================================INTERPOLATION OF ZMAT-Files=================================================================#
#============================================================================================================================================================#
def interpolate(start, end,natoms,n_singlets,n_triplets):
  #first change xyz files to Zmat files
  os.system("obabel -ixyz %s -ogzmat -O start.zmat" %(start))
  os.system("obabel -ixyz %s -ogzmat -O end.zmat" %(end))
  os.system("tail -n +6 start.zmat > start_1.zmat" ) 
  os.system("tail -n +6 end.zmat > end_1.zmat" )
  #nmstates = Restart_Properties['nmstates']
  #natoms = Restart_Properties['natoms']
  natoms = natoms
  nmstates = 33
  #read files
  scanpath=os.getcwd()
  f1=open(scanpath+'/start_1.zmat', 'r')
  data1=f1.readlines()
  f1.close()

  f2=open(scanpath+'/end_1.zmat', 'r')
  data2=f2.readlines()
  f2.close()

  #parse files
  res1=read_zmat(data1)
  res2=read_zmat(data2)
  #if res1['header']!=res2['header']:
    #print 'Problem with headers!'
    #sys.exit(1)

  #prepare interpolation
  base = 'interpolate'
  nsteps=int(30)
  #iinterpolate and write files
  for istep in range(nsteps):
    string='#\n\ntitle\n\n0 0\n'+''.join(res1['header'])
    string+='\n'
    for i in res1:
      if i=='header':
        continue
      f=interpol(res1[i],res2[i],istep,nsteps)
      string+='%s %20.12f\n' % (i,f)
    string+='\n\n\n'
    filename=scanpath+'/'+base+str(istep)+'.zmat'
    fi=open(filename,'w')
    fi.write(string)
    fi.close

  #changes files from zmat to xyz-files and append files to make valid QM.in
  i=int(0)
  laststep=int(nsteps)-1
  while True:
    if i<laststep:
      os.system("obabel -igzmat %s/interpolate%i.zmat -oxyz -O %s/interpolate%i.xyz" %(scanpath,i,scanpath,i))
      #make alignment to first xyz-file
      if i==0:
        #make an alignment-file once
        write_alignsh(natoms,scanpath)
        #read QM.out from starting geometry (ICOND_00000) to get the initial velocity vector
        #Properties['0']={}
        #Properties=read_QMinit_out(scanpath,Properties)
      cwd=os.getcwd()
      os.system("bash %s/align.sh %s/start.xyz %s/%s" %(scanpath, scanpath, scanpath, base+str(i)+'.xyz'))
      #append files with QM.in string
      file=open(scanpath+'/interpolate'+str(i)+'.xyz', 'a')
      #file.write(string_QMin)
      file.close()
      i+=1
    elif i>=laststep:
      break
  #make the last file separately since it is not working otherwise
  os.system("obabel -igzmat %s/end.zmat -oxyz -O %s/interpolate%i.xyz" %(scanpath,scanpath,laststep))
  os.system("bash %s/align.sh %s/start.xyz %s/%s" %(scanpath,scanpath,scanpath,base+str(laststep)+'.xyz'))
  #file = open(scanpath+'/interpolate'+str(laststep)+'.xyz','a')
  #file.write(string_QMin)
  #file.close()
  #qm_calc(scanpath, laststep,n_singlets,n_triplets)
  #Properties,OUTPUT=phasecorrection(Properties, QMpath, NNpath, scanpath, laststep, NNpath_superior, nsteps)
  #generate one output.dat file containing all interpolated geometries
  #generate_outputdat(scanpath+'/QM/', nsteps)
  #generate_phasevector(Properties,laststep,trajpath,nmstates)
  #rm QM.out files
  #TODO put # away of the 2 following lines
  #for i in range(1,nsteps):
    #os.system( 'rm %s/QM/QM%i~.out %s/QM/QM%i.out' %(scanpath,i,scanpath,i))

 
def read_zmat(data):
  res={'header':[]}
  for iline,line in enumerate(data):
    if line.strip()=='':
      res['header'].append(line)
    else:
      break
  for iline, line in enumerate(data):
  #while True:
    if iline==len(data):
      break
    line=data[iline]
    if line.startswith('Variables:'):
      iline+=1
      for index in range(iline,len(data)-1):
        line=data[index]
        s=line.split()
        res[s[0]]=float(s[1])
      break
    else:
      res['header'].append(line)
    iline+=1
  return res

def interpol(x,y,istep,nsteps):
  short_angle=((y-x)+180.)%360.-180.
  #print short_angle
  return x + short_angle*istep/(nsteps-1)

def write_alignsh(natoms,scanpath):
  string=''
  natoms_2=int(natoms)-int(1)
  string+='n=%i\n' %natoms
  string+='m=$(echo "$n-1"|bc)\n'
  string+='q="index 0 to %i"\n' %natoms_2
  string+='xyz1=$1\n'
  string+='xyz2=$2\n\n'
  string+='#write VMD input\n'
  string+='echo "\n'
  string+='mol new \%s$2\%s\n' %('"','"')
  string+='mol new \%s$1\%s\n\n'%('"','"')
  string+='set sel0 [atomselect 0 \%s$q\%s]\n' %('"','"')
  string+='set sel0_ [atomselect 0 \%sall\%s]\n'%('"','"')
  string+='set sel1 [atomselect 1 \%s$q\%s]\n'%('"','"')
  string+='set M [measure fit \$sel0 \$sel1]\n'
  string+='\$sel0_ move \$M\n\n'
  string+='\$sel0_ writepdb \%stmp.pdb\%s\n'%('"','"')
  string+='quit\n'
  string+='" > tmp.vmd\n\n'
  string+='#run VMD\n'
  string+='vmd -e tmp.vmd -dispdev text $> /dev/null\n'
  string+='rm tmp.vmd\n\n'
  string+='#convert with obabel\n'
  string+='obabel -ipdb tmp.pdb -oxyz -O $2\n'
  string+='rm tmp.pdb\n'
  alignfile=open(scanpath+'/align.sh', 'w')
  alignfile.write(string)
  alignfile.close()




