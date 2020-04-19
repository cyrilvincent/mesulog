using NumSharp;
using Tensorflow;
using static Tensorflow.Binding;

namespace PlayerConsole
{
    public class ImageRecognition
    {
        public NDArray[] Run(string file)
        {
            Graph graph = new Graph();
            byte[] bytes = LoadModel.Load();
            graph.Import(bytes, "");
            Operation operationIn = graph.OperationByName("conv2d_1_input");
            Operation operationOut = graph.OperationByName("dense_2/Softmax");
            NDArray ndArray = ReadTensorFromImageFile(file);
            using (Session session = tf.Session(graph))
                return session.run(operationOut.outputs, (FeedItem)(operationIn.outputs[0], ndArray));
            
        }

        private NDArray ReadTensorFromImageFile(
          string file_name,
          int input_height = 64,
          int input_width = 64,
          int input_mean = 0,
          int input_std = 255)
        {
            var graph = tf.Graph().as_default();

            var file_reader = tf.read_file(file_name, "file_reader");
            var decodeJpeg = tf.image.decode_jpeg(file_reader, channels: 1, name: "DecodeJpeg");
            var cast = tf.cast(decodeJpeg, tf.float32);
            var dims_expander = tf.expand_dims(cast, 0);
            var resize = tf.constant(new int[] { input_height, input_width });
            var bilinear = tf.image.resize_bilinear(dims_expander, resize);
            var sub = tf.subtract(bilinear, new float[] { input_mean });
            var normalized = tf.divide(sub, new float[] { input_std });

            using (var sess = tf.Session(graph))
                return sess.run(normalized);
        }
    }
}
