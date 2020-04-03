"""
This module is used to represent an Image object from the DICOMImages table in the database.
"""

from typing import Optional

import pydicom


class Image:
    """
    This class stores all information about an image from the DICOMImages table in the database.
    """

    def __init__(self, instance: str, class_ui: str, number: str, date: str, time: str, echo_number: str,
                 number_of_frames: str, acq_date: str, acq_time: str, receiving_c: str, acq_number: str,
                 slice_location: str, samples_per: str, photo_metric: str, rows: str, columns: str, bits_stored: str,
                 image_type: str, identity: str, object_file: str, device_name: str,
                 content: Optional[pydicom.FileDataset] = None):
        """
        The constructor of the Image class.
        :param instance: The instance of the image.
        :param class_ui: The class_ui of the image.
        :param number: The number of the image.
        :param date: The date of the image.
        :param time: The time of the image.
        :param echo_number: The echo number of the image.
        :param number_of_frames: The number of frames of the image.
        :param acq_date: The acq date of the image.
        :param acq_time: The acq time of the image.
        :param receiving_c: The receiving c of the image.
        :param acq_number: The acq number of the image.
        :param slice_location: The slice location of the image.
        :param samples_per: The samples per of the image.
        :param photo_metric: The photo metric of the image.
        :param rows: The rows of the image.
        :param columns: The columns of the image.
        :param bits_stored: The bits stored of the image.
        :param image_type: The image type of the image.
        :param identity: The identity of the image.
        :param object_file: The object file of the image.
        :param device_name: The device name of the image.
        :param content: The content of the image.
        """

        # all fields that are used for storing the properties of the image.
        self._instance: str = instance
        self._class_ui: str = class_ui
        self._number: str = number
        self._date: str = date
        self._time: str = time
        self._echo_number: str = echo_number
        self._number_of_frames: str = number_of_frames
        self._acq_date: str = acq_date
        self._acq_time: str = acq_time
        self._receiving_c: str = receiving_c
        self._acq_number: str = acq_number
        self._slice_location: str = slice_location
        self._samples_per: str = samples_per
        self._photo_metric: str = photo_metric
        self._rows: str = rows
        self._columns: str = columns
        self._bits_stored: str = bits_stored
        self._image_type: str = image_type
        self._identity: str = identity
        self._object_file: str = object_file
        self._device_name: str = device_name
        self._content: Optional[pydicom.FileDataset] = content
    
    @property
    def instance(self) -> str:
        """
        The get method of the instance property.
        :return: The value of the _instance field.
        """
        return self._instance
    
    @instance.setter
    def instance(self, value: str) -> None:
        """
        The set method of the instance property.
        :param value: The new value for the instance property
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._instance: str = value
    
    @property
    def class_ui(self) -> str:
        """
        The get method of the class_ui property.
        :return: The value of the _class_ui field.
        """
        return self._class_ui
    
    @class_ui.setter
    def class_ui(self, value: str) -> None:
        """
        The set method of the class_ui property.
        :param value: The new value for the class_ui property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._class_ui: str = value
    
    @property
    def number(self) -> str:
        """
        The get method of the number property.
        :return: The value of the _number field.
        """
        return self._number
    
    @number.setter
    def number(self, value: str) -> None:
        """
        The set method of the number property.
        :param value: The new value for the number property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._number: str = value
    
    @property
    def date(self) -> str:
        """
        The get method of the date property.
        :return: The value of the _date field.
        """
        return self._date
    
    @date.setter
    def date(self, value: str) -> None:
        """
        The set method of the date property.
        :param value: The new value for the date property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._date: str = value

    @property
    def time(self) -> str:
        """
        The get method of the time property.
        :return: The value of the _time field.
        """
        return self._time

    @time.setter
    def time(self, value: str) -> None:
        """
        The set method of the time property.
        :param value: The new value for the time property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._time: str = value
    
    @property
    def echo_number(self) -> str:
        """
        The get method of the echo_number property.
        :return: The value of the _echo_number field.
        """
        return self._echo_number

    @echo_number.setter
    def echo_number(self, value: str) -> None:
        """
        The set method of the echo_number property.
        :param value: The new value for the echo_number property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._echo_number: str = value
        
    @property
    def number_of_frames(self) -> str:
        """
        The get method of the number_of_frames property.
        :return: The value of the _number_of_frames field.
        """
        return self._number_of_frames
    
    @number_of_frames.setter
    def number_of_frames(self, value: str) -> None:
        """
        The set method of the number_of_frames property.
        :param value: The new value for the number_of_frames property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._number_of_frames: str = value
    
    @property
    def acq_date(self) -> str:
        """
        The get method of the acq_date property.
        :return: The value of the _acq_date field.
        """
        return self._acq_date
    
    @acq_date.setter
    def acq_date(self, value: str) -> None:
        """
        The set method of the acq_date property.
        :param value: The new value for the acq_date property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._acq_date: str = value
    
    @property
    def acq_time(self) -> str:
        """
        The get method of the acq_time property.
        :return: The value of the _acq_time field.
        """
        return self._acq_time
    
    @acq_time.setter
    def acq_time(self, value: str) -> None:
        """
        The set method of the acq_time property.
        :param value: The new value for the acq_time property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._acq_time: str = value
    
    @property
    def receiving_c(self) -> str:
        """
        The get method of the receiving_c property.
        :return: The value of the _receiving_c field.
        """
        return self._receiving_c
    
    @receiving_c.setter
    def receiving_c(self, value: str) -> None:
        """
        The set method of the receiving_c property.
        :param value: The new value for the receiving_c property.
        :return: The method doesn't return anything
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._receiving_c: str = value
    
    @property
    def acq_number(self) -> str:
        """
        The get method of the acq_number property.
        :return: The value of the _acq_number field.
        """
        return self._acq_number
    
    @acq_number.setter
    def acq_number(self, value: str) -> None:
        """
        The set method of the acq_number property.
        :param value: The new value for the acq_number property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._acq_number: str = value
    
    @property
    def slice_location(self) -> str:
        """
        The get method of the slice_location property.
        :return: The value of the _slice_location field.
        """
        return self._slice_location
    
    @slice_location.setter
    def slice_location(self, value: str) -> None:
        """
        The set method of the slice_location property.
        :param value: The new value for the slice_location property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._slice_location: str = value
        
    @property
    def samples_per(self) -> str:
        """
        The get method of the samples_per property.
        :return: The value of the _samples_per field.
        """
        return self._samples_per
    
    @samples_per.setter
    def samples_per(self, value: str) -> None:
        """
        The set method of the samples_per property.
        :param value: The new value for the samples_per property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._samples_per: str = value
    
    @property
    def photo_metric(self) -> str:
        """
        The get method of the photo_metric property.
        :return: The value of the _photo_metric field.
        """
        return self._photo_metric
    
    @photo_metric.setter
    def photo_metric(self, value: str) -> None:
        """
        The set method of the photo_metric property.
        :param value: The new value for the photo_metric property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._photo_metric: str = value
    
    @property
    def rows(self) -> str:
        """
        The get method of the rows property.
        :return: The value of the _rows field.
        """
        return self._rows
    
    @rows.setter
    def rows(self, value: str) -> None:
        """
        The set method of the rows property.
        :param value: The new value of the rows property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._rows: str = value
    
    @property
    def columns(self) -> str:
        """
        The get method of the columns property.
        :return: The value of the _columns field.
        """
        return self._columns
    
    @columns.setter
    def columns(self, value: str) -> None:
        """
        The set method of the columns property.
        :param value: The new value for the columns property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains invalid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._columns: str = value
    
    @property
    def bits_stored(self) -> str:
        """
        The get method of the bits_stored property.
        :return: The value of the _bits_stored field.
        """
        return self._bits_stored
    
    @bits_stored.setter
    def bits_stored(self, value: str) -> None:
        """
        The set method of the bits_stored property.
        :param value: The new value for the bits_stored property.
        :return: The method doesn't return anything.
        """

        # Checks whether the value contains invalid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._bits_stored: str = value
        
    @property
    def image_type(self) -> str:
        """
        The get method of the image_type property.
        :return: The value of the _image_type field.
        """
        return self._image_type
    
    @image_type.setter
    def image_type(self, value: str) -> None:
        """
        The set method of the image_type property.
        :param value: The new value for the image_type property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._image_type: str = value

    @property
    def identity(self) -> str:
        """
        The get method of the identity property.
        :return: The value of the _identity field.
        """
        return self._identity

    @identity.setter
    def identity(self, value: str) -> None:
        """
        The set method of the identity property.
        :param value: The new value for the identity property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._identity: str = value
        
    @property
    def object_file(self) -> str:
        """
        The get method of the object_file property.
        :return: The value of the _object_file field.
        """
        return self._object_file
    
    @object_file.setter
    def object_file(self, value: str) -> None:
        """
        The set method of the object_file property.
        :param value: The new value for the object_file_property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._object_file: str = value

    @property
    def device_name(self) -> str:
        """
        The get method of the device_name property.
        :return: The value of the _device_name field.
        """
        return self._device_name

    @device_name.setter
    def device_name(self, value: str) -> None:
        """
        The set method of the device_name property.
        :param value: The new value for the device_name property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._device_name: str = value

    @property
    def content(self) -> pydicom.FileDataset:
        """
        The get method of the content property.
        :return: The value of the _content field.
        """
        return self._content

    @content.setter
    def content(self, value: pydicom.FileDataset) -> None:
        """
        The set method of the content property.
        :param value: The new value for the content property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._content: pydicom.FileDataset = value

    def __eq__(self, other: object) -> bool:
        """
        Checks whether object is equal to other object.
        Overrides the __eq__ method from the object class.
        :param other: The object to compare to.
        :return: Returns true if objects are equal and false if they aren't equal.
        """

        # Checks whether other object is instance of Image.
        if not isinstance(other, Image):
            return False

        # Checks whether fields are equal.
        if self.instance != other.instance:
            return False
        if self.class_ui != other.class_ui:
            return False
        if self.number != other.number:
            return False
        if self.date != other.date:
            return False
        if self.time != other.time:
            return False
        if self.echo_number != other.echo_number:
            return False
        if self.number_of_frames != other.number_of_frames:
            return False
        if self.acq_date != other.acq_date:
            return False
        if self.acq_time != other.acq_time:
            return False
        if self.receiving_c != other.receiving_c:
            return False
        if self.acq_number != other.acq_number:
            return False
        if self.slice_location != other.slice_location:
            return False
        if self.samples_per != other.samples_per:
            return False
        if self.photo_metric != other.photo_metric:
            return False
        if self.rows != other.rows:
            return False
        if self.columns != other.columns:
            return False
        if self.bits_stored != other.bits_stored:
            return False
        if self.image_type != other.image_type:
            return False
        if self.identity != other.identity:
            return False
        if self.object_file != other.object_file:
            return False
        return self.device_name == other.device_name

    def __hash__(self) -> int:
        """
        Calculates hash value of the object.
        Overrides the __hash__ method from the object class.
        :return: Hash value of the object.
        """
        return hash((self.instance, self.date, self.time, self.object_file))
