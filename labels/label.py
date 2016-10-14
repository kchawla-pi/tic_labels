#!/usr/bin/env python
"""
Label connected components on an image with scipy.ndimage
"""
import sys      
import nibabel 
import scipy.ndimage
import argparse

import labels


def main():

     usage = "usage: %prog [options] arg1 arg2"

     parser = argparse.ArgumentParser(prog='iw_labels_label')

     parser.add_argument("in_nii",    help="Filename of NIFTI input label ")
     parser.add_argument("--out_nii", help="Filename of NIFTI output label. (default = --in ) ", default=None)

     inArgs = parser.parse_args()

     if inArgs.out_nii == None:
          out_filename = inArgs.in_nii
     else:
          out_filename = inArgs.out_nii

     in_nii    = labels.read_nifti_file( inArgs.in_nii, 'Label file does not exist' )
     in_array  = in_nii.get_data()

     out_array, n_out_array = scipy.ndimage.label( in_array )

     nibabel.save( nibabel.Nifti1Image( out_array, in_nii.get_affine()), out_filename )

     return 0 

#
# Main Function
#

if __name__ == "__main__":
     sys.exit(main())
