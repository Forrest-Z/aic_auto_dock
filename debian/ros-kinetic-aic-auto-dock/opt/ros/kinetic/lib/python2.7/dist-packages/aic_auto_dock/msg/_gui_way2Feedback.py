# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from aic_auto_dock/gui_way2Feedback.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class gui_way2Feedback(genpy.Message):
  _md5sum = "92d80fef0082d27f007cd916743cbfcb"
  _type = "aic_auto_dock/gui_way2Feedback"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
uint64              err_msg          #状态码

int32               status
int32               EXECUTING = 1
int32               PAUSE = 2

int32               feedback
int32               OBSTACLE_AVOIDING = 10
int32               AVOID_SUCCESS = 11
int32               ILLEGAL_GOAL = 12
int32               STEP_PROCESS = 13

float32             remaining_distance
int32               step_process
int32               PREPARE_NAV_STEP = 0
int32               PREPARE_STEP = 1
int32               PORT_STEP = 2

"""
  # Pseudo-constants
  EXECUTING = 1
  PAUSE = 2
  OBSTACLE_AVOIDING = 10
  AVOID_SUCCESS = 11
  ILLEGAL_GOAL = 12
  STEP_PROCESS = 13
  PREPARE_NAV_STEP = 0
  PREPARE_STEP = 1
  PORT_STEP = 2

  __slots__ = ['err_msg','status','feedback','remaining_distance','step_process']
  _slot_types = ['uint64','int32','int32','float32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       err_msg,status,feedback,remaining_distance,step_process

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(gui_way2Feedback, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.err_msg is None:
        self.err_msg = 0
      if self.status is None:
        self.status = 0
      if self.feedback is None:
        self.feedback = 0
      if self.remaining_distance is None:
        self.remaining_distance = 0.
      if self.step_process is None:
        self.step_process = 0
    else:
      self.err_msg = 0
      self.status = 0
      self.feedback = 0
      self.remaining_distance = 0.
      self.step_process = 0

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
      buff.write(_get_struct_Q2ifi().pack(_x.err_msg, _x.status, _x.feedback, _x.remaining_distance, _x.step_process))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.err_msg, _x.status, _x.feedback, _x.remaining_distance, _x.step_process,) = _get_struct_Q2ifi().unpack(str[start:end])
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
      buff.write(_get_struct_Q2ifi().pack(_x.err_msg, _x.status, _x.feedback, _x.remaining_distance, _x.step_process))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.err_msg, _x.status, _x.feedback, _x.remaining_distance, _x.step_process,) = _get_struct_Q2ifi().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_Q2ifi = None
def _get_struct_Q2ifi():
    global _struct_Q2ifi
    if _struct_Q2ifi is None:
        _struct_Q2ifi = struct.Struct("<Q2ifi")
    return _struct_Q2ifi