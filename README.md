## Generate RotD Spectra using OpenSeesPython


This code develops the RotD50 Sa and RotD100 Sa Spectra of the Bi-Directional Ground Motion records provided in the 'GM' folder which must be in current folder. The two directions of the ground motion record must be named as 'GM1i' and 'GM2i', where 'i' is the ground motion number which goes from 1 to 'n', 'n' being the total
number of ground motions for which the Spectra needs to be generated. The extension of the files must be '.AT2'

      For example: If the Spectra of two ground motion records are required, 4 files with the following names must be provided in the given 'GM' folder:

      'GM11.AT2' - Ground Motion 1 in direction 1 (direction 1 can be either one of the bi-directional GM as we are rotating the ground motions it does not matter) 

      'GM21.AT2' - Ground Motion 1 in direction 2 (direction 2 is the other direction of the bi-directional GM)

      'GM12.AT2' - Ground Motion 2 in direction 1 (direction 1 can be either one of the bi-directional GM as we are rotating the ground motions it does not matter)  

      'GM22.AT2' - Ground Motion 2 in direction 2 (direction 2 is the other direction of the bi-directional GM)


The Ground Motion file must be a vector file with 4 header lines.The first 3 lines can have any content, however, the 4th header line must be written exactly as per the following example:
  
      'NPTS=  15864, DT= 0.0050'
    
  
INPUT:

This codes provides the option to have 3 different regions of developing the Spectra of ground motions with different period intervals (discretizations) 

The following inputs within the code are required:

        'Path_to_openpyfiles'--> Path where the library files 'opensees.pyd' and 'LICENSE.rst' of OpenSeesPy are included (for further details go to https://openseespydoc.readthedocs.io/en/latest/windows.html)

        'Int_T_Reg_1'        --> Period Interval for the first region of the Spectrum 

        'End_T_Reg_1'        --> Last Period of the first region of the Spectrum (where to end the first region)

        'Int_T_Reg_2'        --> Period Interval for the second region of the Spectrum 

        'End_T_Reg_2'        --> Last Period of the second region of the Spectrum (where to end the second region)

        'Int_T_Reg_3'        --> Period Interval for the third region of the Spectrum 

        'End_T_Reg_3'        --> Last Period of the third region of the Spectrum (where to end the third region)

        'Plot_Spectra'       --> whether to plot the generated Spectra of the ground motions (options: 'Yes', 'No')    


OUTPUT:

The output will be provided in a separate 'GMi_Spectra.txt' file for each ground motion record, where 'i' denotes the number of ground motion in the same of provided 'GM1i.AT2' and 'GM2i.AT2' files. The output files will be generated in a saperate folder 'Spectra' which will be created in the current folder

The 'GMi_Spectra.txt' file will consist of space-separated file with:
    
        'Periods (secs)' 'RotD50 Sa (g)' 'RotD100 Sa (g)' 
    
