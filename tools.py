import struct
import const
from ubluetooth import UUID
PACK = struct.pack
UNPACK = struct.unpack

class BLETools(object):
	"""
	Payload Generator Functions
	"""
	# Advertising payloads are repeated packets of the following form:
	#   1 byte data length (N + 1)
	#   1 byte type (see constants below)
	#   N bytes type-specific data
	@staticmethod
	def advertising_generic_payload(limited_disc=False, br_edr=False, name=None, services=None, appearance=0):
		"""
		Generate a payload to be passed to gap_advertise(adv_data=...).
		"""
		payload = bytearray()

		def _append(adv_type, value):
			nonlocal payload
			payload += PACK('BB', len(value) + 1, adv_type) + value

		_append(const.BLEConst.ADType.AD_TYPE_FLAGS, PACK('B', (0x01 if limited_disc else 0x02) + (0x00 if br_edr else 0x04)))

		if name:
			_append(const.BLEConst.ADType.AD_TYPE_COMPLETE_LOCAL_NAME, name)

		if services:
			for uuid in services:
				b = bytes(uuid)
				if len(b) == 2:
					_append(const.BLEConst.ADType.AD_TYPE_16BIT_SERVICE_UUID_COMPLETE, b)
				elif len(b) == 4:
					_append(const.BLEConst.ADType.AD_TYPE_32BIT_SERVICE_UUID_COMPLETE, b)
				elif len(b) == 16:
					_append(const.BLEConst.ADType.AD_TYPE_128BIT_SERVICE_UUID_COMPLETE, b)

		# See org.bluetooth.characteristic.gap.appearance.xml
		_append(const.BLEConst.ADType.AD_TYPE_APPEARANCE, PACK('<h', appearance))

		return payload

	@staticmethod
	def advertising_resp_payload(name=None, services=None):
		"""
		Generate payload for Scan Response
		"""
		payload = bytearray()

		def _append(adv_type, value):
			nonlocal payload
			payload += PACK('BB', len(value) + 1, adv_type) + value

		if name:
			_append(const.BLEConst.ADType.AD_TYPE_COMPLETE_LOCAL_NAME, name)

		if services:
			for uuid in services:
				b = bytes(uuid)
				if len(b) == 2:
					_append(const.BLEConst.ADType.AD_TYPE_16BIT_SERVICE_UUID_COMPLETE, b)
				elif len(b) == 4:
					_append(const.BLEConst.ADType.AD_TYPE_32BIT_SERVICE_UUID_COMPLETE, b)
				elif len(b) == 16:
					_append(const.BLEConst.ADType.AD_TYPE_128BIT_SERVICE_UUID_COMPLETE, b)

		return payload

	@staticmethod
	def decode_mac(addr):
		"""
		Decode readable mac address from advertising addr
		"""
		if isinstance(addr, memoryview):
			addr = bytes(addr)

		assert isinstance(addr, bytes) and len(addr) == 6, ValueError("mac address value error")
		return ":".join(['%02X' % byte for byte in addr])
	 # speed: 0 ~ 100
        def set_speed(self, speed: int, direction: int):
	        if direction == FORWARD:
	            self.pwm_f.duty_u16(int(_FULL_DUTY * (speed / 100)))
	            self.pwm_b.duty_u16(0)
	        else:
	            self.pwm_f.duty_u16(0)
	            self.pwm_b.duty_u16(int(_FULL_DUTY * (speed / 100)))
	
