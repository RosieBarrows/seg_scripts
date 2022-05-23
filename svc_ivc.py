from img import add_masks
from img import save_itk
import SimpleITK as sitk

import numpy as np
import nrrd
import pylab

seg_corrected_nrrd = '/data/Dropbox/henry/segmentations/seg_corrected.nrrd'

svc_nrrd = '/data/Dropbox/henry/segmentations/SVC.nrrd'
svc_label = '13'

ivc_nrrd = '/data/Dropbox/henry/segmentations/IVC.nrrd'
ivc_label = '14'

seg_corrected_array, header1 = nrrd.read(seg_corrected_nrrd)
svc_array, header2 = nrrd.read(svc_nrrd)
ivc_array, header3 = nrrd.read(ivc_nrrd)

print(header1['axis mins'])
print(header1['spacings'])
print(header2['axis mins'])
print(header2['spacings'])
print(header3['axis mins'])
print(header3['spacings'])

seg_corrected_svc = add_masks(seg_corrected_array, svc_array, svc_label)
seg_corrected_svc_ivc = add_masks(seg_corrected_svc, ivc_array, ivc_label)

save_itk(seg_corrected_svc_ivc, header1['axis mins'], header1['spacings'], '/data/Dropbox/henry/segmentations/seg_svc_ivc.nrrd')
