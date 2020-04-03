setlocal DisableDelayedExpansion

 

set "search=HOME"

set replace=%cd%

del conquest\dicom.ini

for /F "delims=" %%a in (conquest\dicom_template.ini) DO (

   set line=%%a

   setlocal EnableDelayedExpansion

   >> conquest\dicom.ini echo(!line:%search%=%replace%!

   endlocal

)


