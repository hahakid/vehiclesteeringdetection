import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class pos320(genpy.Message):
  _md5sum = "90a0b5614d459b65b16442e42c81a2f7"
  _type = "zf_msgs/pos320"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
uint8 length
uint8 mode
int16 time1
int32 time2
uint8 num
float64 lat
float64 lon
float64 height
float64 v_n
float64 v_e
float64 v_earth
float64 roll
float64 pitch
float64 head
float64 a_n
float64 a_e
float64 a_earth
float64 v_roll
float64 v_pitch
float64 v_head
uint8 status1
uint8 status2
uint8 checksum
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
  __slots__ = ['header','length','mode','time1','time2','num','lat','lon','height','v_n','v_e','v_earth','roll','pitch','head','a_n','a_e','a_earth','v_roll','v_pitch','v_head','status1','status2','checksum']
  _slot_types = ['std_msgs/Header','uint8','uint8','int16','int32','uint8','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    The available fields are:
       header,length,mode,time1,time2,num,lat,lon,height,v_n,v_e,v_earth,roll,pitch,head,a_n,a_e,a_earth,v_roll,v_pitch,v_head,status1,status2,checksum
    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(pos320, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.length is None:
        self.length = 0
      if self.mode is None:
        self.mode = 0
      if self.time1 is None:
        self.time1 = 0
      if self.time2 is None:
        self.time2 = 0
      if self.num is None:
        self.num = 0
      if self.lat is None:
        self.lat = 0.
      if self.lon is None:
        self.lon = 0.
      if self.height is None:
        self.height = 0.
      if self.v_n is None:
        self.v_n = 0.
      if self.v_e is None:
        self.v_e = 0.
      if self.v_earth is None:
        self.v_earth = 0.
      if self.roll is None:
        self.roll = 0.
      if self.pitch is None:
        self.pitch = 0.
      if self.head is None:
        self.head = 0.
      if self.a_n is None:
        self.a_n = 0.
      if self.a_e is None:
        self.a_e = 0.
      if self.a_earth is None:
        self.a_earth = 0.
      if self.v_roll is None:
        self.v_roll = 0.
      if self.v_pitch is None:
        self.v_pitch = 0.
      if self.v_head is None:
        self.v_head = 0.
      if self.status1 is None:
        self.status1 = 0
      if self.status2 is None:
        self.status2 = 0
      if self.checksum is None:
        self.checksum = 0
    else:
      self.header = std_msgs.msg.Header()
      self.length = 0
      self.mode = 0
      self.time1 = 0
      self.time2 = 0
      self.num = 0
      self.lat = 0.
      self.lon = 0.
      self.height = 0.
      self.v_n = 0.
      self.v_e = 0.
      self.v_earth = 0.
      self.roll = 0.
      self.pitch = 0.
      self.head = 0.
      self.a_n = 0.
      self.a_e = 0.
      self.a_earth = 0.
      self.v_roll = 0.
      self.v_pitch = 0.
      self.v_head = 0.
      self.status1 = 0
      self.status2 = 0
      self.checksum = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2BhiB15d3B().pack(_x.length, _x.mode, _x.time1, _x.time2, _x.num, _x.lat, _x.lon, _x.height, _x.v_n, _x.v_e, _x.v_earth, _x.roll, _x.pitch, _x.head, _x.a_n, _x.a_e, _x.a_earth, _x.v_roll, _x.v_pitch, _x.v_head, _x.status1, _x.status2, _x.checksum))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 132
      (_x.length, _x.mode, _x.time1, _x.time2, _x.num, _x.lat, _x.lon, _x.height, _x.v_n, _x.v_e, _x.v_earth, _x.roll, _x.pitch, _x.head, _x.a_n, _x.a_e, _x.a_earth, _x.v_roll, _x.v_pitch, _x.v_head, _x.status1, _x.status2, _x.checksum,) = _get_struct_2BhiB15d3B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2BhiB15d3B().pack(_x.length, _x.mode, _x.time1, _x.time2, _x.num, _x.lat, _x.lon, _x.height, _x.v_n, _x.v_e, _x.v_earth, _x.roll, _x.pitch, _x.head, _x.a_n, _x.a_e, _x.a_earth, _x.v_roll, _x.v_pitch, _x.v_head, _x.status1, _x.status2, _x.checksum))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 132
      (_x.length, _x.mode, _x.time1, _x.time2, _x.num, _x.lat, _x.lon, _x.height, _x.v_n, _x.v_e, _x.v_earth, _x.roll, _x.pitch, _x.head, _x.a_n, _x.a_e, _x.a_earth, _x.v_roll, _x.v_pitch, _x.v_head, _x.status1, _x.status2, _x.checksum,) = _get_struct_2BhiB15d3B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2BhiB15d3B = None
def _get_struct_2BhiB15d3B():
    global _struct_2BhiB15d3B
    if _struct_2BhiB15d3B is None:
        _struct_2BhiB15d3B = struct.Struct("<2BhiB15d3B")
    return _struct_2BhiB15d3B
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I