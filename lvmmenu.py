import os
os.system("tput setaf 6")
print("\t\t\tWelcome to the Menu")
os.system("tput setaf 7")
print("\t\t\t--------------------")
print("\n\n\n")
f="y"
while True:
	if "y" in f:
		os.system("clear")		
		print("Press 1 : to know how many virtual harddisk are there")
		print("Press 2 : to know all about the filesystems present in system")
		print("Press 3 : to make physical volume from the no of disk as you want")
		print("Press 4 : to know whether phycical volume is created or not")
		print("Press 5 : to create volume group from the physical volume created")
		print("Press 6 : to know whether volume group is created or not")
		print("Press 7 : to make partition of volume group created")
		print("Press 8 : to format the partitions created")
		print("Press 9 : to mount the partitions created")
		print("press 10 : to extend the partion size")
		print("Press 11 : to reduce the partition size")
		print("Press 12 : to know about the partition whether the partion is created/mounted or not")
		c=input("Enter your choice : ")
		print(c)
		if int(c)==1:
				os.system("fdisk -l")
		elif int(c)==2:
				os.system("df -hT")
		elif int(c)==3:
				j=input("no of disks from which you wanna make physical volume : ")
				for i in range(int(j)):
					print("type the disk name to create physical volume : ")
					diskname = input()
					os.system("pvcreate "+diskname)		 
		elif int(c)==4:
				os.system("pvdisplay")
		elif int(c)==5:
				t=input("no. of pvs from which you wanna make vg : ")
				q=" "
				for r in range(int(t)):
					pvname = input("type your pv name : " )
					q=q+" "+pvname
				print(q)
				vgname = input("type the name of vg you want to create : ")
				os.system("vgcreate "+vgname+" "+q)
		elif int(c)==6:
				os.system("vgdisplay")
		elif int(c)==7:
				print("type the size in Gb/Mb to create partiton.. specify Mb as M and 					Gb as G")		
				s=input()
				print("type the name of partition that you wish to create")
				prtnname=input()
				os.system("lvcreate --size "+s+ "--name" +prtnname+" "+vgname)
		elif int(c)==8:
				os.system("mkfs.ext4  /dev/"+vgname+"/"+prtnname)
		elif int(c)==9:
				vgname=input("type the volume group name : ")
				prtnname=input("type the partition name : ")
				print("type the name of directory to mount ")
				dirname=input()
				os.system("mkdir "+dirname)
				os.system("mount /dev/"+vgname+"/"+prtnname+"+/"+dirname)
		elif int(c)==10:
				vgname=input("type the volume group name : ")
				prtnname=input("type the partition name : ")
				print("type the size in gb by which you wish to extend the size")
				esize=input()
				os.system("lvextend --size +"+esize+" /dev/"+vgname+"+/"+prtnname)
				os.system("resize2fs /dev/"+vgname+"+/"+prtnname)
		elif int(c)==11:
				vgname=input("type the volume group name : ")
				prtnname=input("type the partition name : ")
				print("type the size by which you wish to reduce the size ..specify Mb 					as M and Gb as G")
				rs=input()
				os.system("unmount /dev/"+vgname+"/"+prtnname+"+/"+dirname)
				os.system("lvreduce --size +"+rs+" /dev/"+vgname+"+/"+prtnname1)
		elif int(c==12):
				os.system("df -h")
		else:
				print("System could not able to find specified cmd")
		f=input("to continue : y/n : ")
	elif "n" in f:
		break
	else:
		print("you can use only y or n")
		f=input("to continue : y/n : ")
