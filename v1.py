import struct
import os
import platform
import time

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def banner():
  banner = ''' *******     *******   **       **     **
/**////**   **/////** /**      //**   ** 
/**    /** **     //**/**       //** **  
/**    /**/**      /**/**        //***   
/**    /**/**      /**/**         **/**  
/**    ** //**     ** /**        ** //** 
/*******   //*******  /******** **   //**
///////     ///////   //////// //     // '''
  print(f"{banner}\n\n")

def option1():
  file_name = input("==============FILE NAME: ")
  if file_name == "99" or file_name == "" or file_name == " ":
    clear()
    exit()
  content = input("==============DOL CONTENT: ")
  if content == "99" or content == "" or content == " ":
    clear()
    exit()
  
  with open(f'{file_name}.dol', 'wb') as output_file:
      header = bytearray(256)
      header[:3] = b'DOL'
      entry_point_offset = 0x18
      num_sections = 3
      bss_size = 0x800
      rel_offset = 0x1C
      imp_offset = 0x24
      bss_offset = 0x34
      struct.pack_into('>i', header, entry_point_offset, entry_point_offset)
      struct.pack_into('>i', header, 0x4, num_sections)
      struct.pack_into('>i', header, 0x10, bss_size)
      struct.pack_into('>i', header, rel_offset, rel_offset)
      struct.pack_into('>i', header, imp_offset, imp_offset)
      struct.pack_into('>i', header, bss_offset, bss_offset)
      output_file.write(header)
      section1 = bytearray(2048)
      section2 = bytearray(2048)
      section3 = bytearray(2048)
      output_file.write(section1)
      output_file.write(section2)
      output_file.write(section3)
      bss = bytearray(2048)
      output_file.write(bss)
  
  time.sleep(1)
  clear()
  print("==============DOL FILE GENERATED!")
  input()
  clear()

def option2():
  file_name = input("==============FILE NAME: ")
  if file_name == "99" or file_name == "" or file_name == " ":
    clear()
    exit()
  content = input("==============ELF CONTENT: ")
  if content == "99" or content == "" or content == " ":
    clear()
    exit()
  
  with open(f'{file_name}.elf', 'wb') as output_file:
      header = bytearray(256)
      header[:3] = b'DOL'
      entry_point_offset = 0x18
      num_sections = 3
      bss_size = 0x800
      rel_offset = 0x1C
      imp_offset = 0x24
      bss_offset = 0x34
      struct.pack_into('>i', header, entry_point_offset, entry_point_offset)
      struct.pack_into('>i', header, 0x4, num_sections)
      struct.pack_into('>i', header, 0x10, bss_size)
      struct.pack_into('>i', header, rel_offset, rel_offset)
      struct.pack_into('>i', header, imp_offset, imp_offset)
      struct.pack_into('>i', header, bss_offset, bss_offset)
      output_file.write(header)
      section1 = bytearray(2048)
      section2 = bytearray(2048)
      section3 = bytearray(2048)
      output_file.write(section1)
      output_file.write(section2)
      output_file.write(section3)
      bss = bytearray(2048)
      output_file.write(bss)
  
  time.sleep(1)
  clear()
  print("==============ELF FILE GENERATED!")
  input()
  clear()

def option3():
  file_name = input("==============FILE NAME: ")
  if file_name == "99" or file_name == "" or file_name == " ":
    clear()
    exit()
  content = input("==============WAD CONTENT: ")
  if content == "99" or content == "" or content == " ":
    clear()
    exit()
  
  with open(f'{file_name}.wad', 'wb') as output_file:
      header = bytearray(256)
      header[:3] = b'DOL'
      entry_point_offset = 0x18
      num_sections = 3
      bss_size = 0x800
      rel_offset = 0x1C
      imp_offset = 0x24
      bss_offset = 0x34
      struct.pack_into('>i', header, entry_point_offset, entry_point_offset)
      struct.pack_into('>i', header, 0x4, num_sections)
      struct.pack_into('>i', header, 0x10, bss_size)
      struct.pack_into('>i', header, rel_offset, rel_offset)
      struct.pack_into('>i', header, imp_offset, imp_offset)
      struct.pack_into('>i', header, bss_offset, bss_offset)
      output_file.write(header)
      section1 = bytearray(2048)
      section2 = bytearray(2048)
      section3 = bytearray(2048)
      output_file.write(section1)
      output_file.write(section2)
      output_file.write(section3)
      bss = bytearray(2048)
      output_file.write(bss)
  
  time.sleep(1)
  clear()
  print("==============DOL FILE GENERATED!")
  input()
  clear()

while True:
  clear()
  time.sleep(0)
  banner()
  print("\tCREATE DOL [1]")
  print("\tCREATE ELF [2]")
  print("\tCREATE WAD [3]")
  option = input("==============OPTION: ")
  if option == "99":
    time.sleep(0)
    clear()
    exit()
  elif option == "1":
    time.sleep(0)
    clear()
    option1()
  elif option == "2":
    time.sleep(0)
    clear()
    option2()
  elif option == "3":
    time.sleep(0)
    clear()
    option3()