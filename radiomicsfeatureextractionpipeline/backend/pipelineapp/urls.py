from django.conf.urls import url
from pipelineapp import views

urlpatterns = [
    url(r"^images/$", views.image_list),
    url(r"^patients/$", views.patient_list),
    url(r"^radiomic-class/$", views.radiomic_class_list),
    url(r"^radiomic-filter/$", views.radiomic_filter_list),
    url(r"^radiomics/$", views.radiomics_list),
    url(r"^roi/$", views.roi_list),
    url(r"^series/$", views.series_list),
    url(r"^series-roi/$", views.series_roi_list),
    url(r"^study/$", views.study_list),
    url(r"^feature/$", views.feature_list),
    url(r"^feature-value/$", views.feature_value_list),
    url(r"^parameter-file/$", views.open_parameter_file),
    url(r"^config-file/$", views.open_config_file),
    url(r"^write-config/$", views.write_to_config_file),
    url(r"^write-params/$", views.write_to_parameter_file),
    url(r"^restore-default-config/$", views.restore_default_config_file),
    url(r"^restore-default-params/$", views.restore_default_parameter_file),
    url(r"^restore-old-config/$", views.restore_old_config_file),
    url(r"^restore-old-params/$", views.restore_old_parameter_file),
    url(r"^priority-setter/$", views.roi_list),
    url(r"^recreate-radiomic-tables/$", views.recreate_radiomic_tables),
    url(r"^download-csv/$", views.download_csv_files),
    url(r"^download-logs/$", views.download_log_files),
    url(r"^delete-calc/$", views.delete_calculation),
    url(r"^start-recalculate/$", views.start_recalculate),
    url(r"^start-calculate/$", views.start_calculate),
    url(r"^cancel/$", views.cancel),
    url(r"^progress/$", views.progress),
    url(r"^calc-list/$", views.get_calculations),
    url(r"^change-priority/$", views.update_priority),
    url(r"^delete-csv/$", views.delete_csv_files),
    url(r"^ping/$", views.pong),
    url(r"^overview/$", views.general_overview),

]
