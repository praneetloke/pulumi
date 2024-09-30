// source: pulumi/errors.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

var jspb = require('google-protobuf');
var goog = jspb;
var proto = { pulumirpc: { codegen: { }, testing: { } } }, global = proto;

goog.exportSymbol('proto.pulumirpc.ErrorCause', null, global);
goog.exportSymbol('proto.pulumirpc.InputPropertiesError', null, global);
goog.exportSymbol('proto.pulumirpc.InputPropertiesError.PropertyError', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.pulumirpc.ErrorCause = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.pulumirpc.ErrorCause, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.pulumirpc.ErrorCause.displayName = 'proto.pulumirpc.ErrorCause';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.pulumirpc.InputPropertiesError = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.pulumirpc.InputPropertiesError.repeatedFields_, null);
};
goog.inherits(proto.pulumirpc.InputPropertiesError, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.pulumirpc.InputPropertiesError.displayName = 'proto.pulumirpc.InputPropertiesError';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.pulumirpc.InputPropertiesError.PropertyError = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.pulumirpc.InputPropertiesError.PropertyError, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.pulumirpc.InputPropertiesError.PropertyError.displayName = 'proto.pulumirpc.InputPropertiesError.PropertyError';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.pulumirpc.ErrorCause.prototype.toObject = function(opt_includeInstance) {
  return proto.pulumirpc.ErrorCause.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.pulumirpc.ErrorCause} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.ErrorCause.toObject = function(includeInstance, msg) {
  var f, obj = {
    message: jspb.Message.getFieldWithDefault(msg, 1, ""),
    stacktrace: jspb.Message.getFieldWithDefault(msg, 2, "")
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.pulumirpc.ErrorCause}
 */
proto.pulumirpc.ErrorCause.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.pulumirpc.ErrorCause;
  return proto.pulumirpc.ErrorCause.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.pulumirpc.ErrorCause} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.pulumirpc.ErrorCause}
 */
proto.pulumirpc.ErrorCause.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setMessage(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setStacktrace(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.pulumirpc.ErrorCause.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.pulumirpc.ErrorCause.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.pulumirpc.ErrorCause} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.ErrorCause.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getMessage();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getStacktrace();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
};


/**
 * optional string message = 1;
 * @return {string}
 */
proto.pulumirpc.ErrorCause.prototype.getMessage = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.ErrorCause} returns this
 */
proto.pulumirpc.ErrorCause.prototype.setMessage = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string stackTrace = 2;
 * @return {string}
 */
proto.pulumirpc.ErrorCause.prototype.getStacktrace = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.ErrorCause} returns this
 */
proto.pulumirpc.ErrorCause.prototype.setStacktrace = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.pulumirpc.InputPropertiesError.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.pulumirpc.InputPropertiesError.prototype.toObject = function(opt_includeInstance) {
  return proto.pulumirpc.InputPropertiesError.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.pulumirpc.InputPropertiesError} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.InputPropertiesError.toObject = function(includeInstance, msg) {
  var f, obj = {
    errorsList: jspb.Message.toObjectList(msg.getErrorsList(),
    proto.pulumirpc.InputPropertiesError.PropertyError.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.pulumirpc.InputPropertiesError}
 */
proto.pulumirpc.InputPropertiesError.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.pulumirpc.InputPropertiesError;
  return proto.pulumirpc.InputPropertiesError.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.pulumirpc.InputPropertiesError} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.pulumirpc.InputPropertiesError}
 */
proto.pulumirpc.InputPropertiesError.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.pulumirpc.InputPropertiesError.PropertyError;
      reader.readMessage(value,proto.pulumirpc.InputPropertiesError.PropertyError.deserializeBinaryFromReader);
      msg.addErrors(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.pulumirpc.InputPropertiesError.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.pulumirpc.InputPropertiesError.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.pulumirpc.InputPropertiesError} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.InputPropertiesError.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getErrorsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.pulumirpc.InputPropertiesError.PropertyError.serializeBinaryToWriter
    );
  }
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.pulumirpc.InputPropertiesError.PropertyError.prototype.toObject = function(opt_includeInstance) {
  return proto.pulumirpc.InputPropertiesError.PropertyError.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.pulumirpc.InputPropertiesError.PropertyError} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.InputPropertiesError.PropertyError.toObject = function(includeInstance, msg) {
  var f, obj = {
    propertyPath: jspb.Message.getFieldWithDefault(msg, 1, ""),
    reason: jspb.Message.getFieldWithDefault(msg, 2, "")
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.pulumirpc.InputPropertiesError.PropertyError}
 */
proto.pulumirpc.InputPropertiesError.PropertyError.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.pulumirpc.InputPropertiesError.PropertyError;
  return proto.pulumirpc.InputPropertiesError.PropertyError.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.pulumirpc.InputPropertiesError.PropertyError} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.pulumirpc.InputPropertiesError.PropertyError}
 */
proto.pulumirpc.InputPropertiesError.PropertyError.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setPropertyPath(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setReason(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.pulumirpc.InputPropertiesError.PropertyError.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.pulumirpc.InputPropertiesError.PropertyError.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.pulumirpc.InputPropertiesError.PropertyError} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.InputPropertiesError.PropertyError.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getPropertyPath();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getReason();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
};


/**
 * optional string property_path = 1;
 * @return {string}
 */
proto.pulumirpc.InputPropertiesError.PropertyError.prototype.getPropertyPath = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.InputPropertiesError.PropertyError} returns this
 */
proto.pulumirpc.InputPropertiesError.PropertyError.prototype.setPropertyPath = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string reason = 2;
 * @return {string}
 */
proto.pulumirpc.InputPropertiesError.PropertyError.prototype.getReason = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.InputPropertiesError.PropertyError} returns this
 */
proto.pulumirpc.InputPropertiesError.PropertyError.prototype.setReason = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * repeated PropertyError errors = 1;
 * @return {!Array<!proto.pulumirpc.InputPropertiesError.PropertyError>}
 */
proto.pulumirpc.InputPropertiesError.prototype.getErrorsList = function() {
  return /** @type{!Array<!proto.pulumirpc.InputPropertiesError.PropertyError>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.pulumirpc.InputPropertiesError.PropertyError, 1));
};


/**
 * @param {!Array<!proto.pulumirpc.InputPropertiesError.PropertyError>} value
 * @return {!proto.pulumirpc.InputPropertiesError} returns this
*/
proto.pulumirpc.InputPropertiesError.prototype.setErrorsList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.pulumirpc.InputPropertiesError.PropertyError=} opt_value
 * @param {number=} opt_index
 * @return {!proto.pulumirpc.InputPropertiesError.PropertyError}
 */
proto.pulumirpc.InputPropertiesError.prototype.addErrors = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.pulumirpc.InputPropertiesError.PropertyError, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.pulumirpc.InputPropertiesError} returns this
 */
proto.pulumirpc.InputPropertiesError.prototype.clearErrorsList = function() {
  return this.setErrorsList([]);
};


goog.object.extend(exports, proto.pulumirpc);
