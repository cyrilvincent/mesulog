using NumSharp;
using System;

namespace PlayerConsole
{
    class Program
    {
        private static void Main(string[] args)
        {
            Console.WriteLine("Predict");
            string file = args[0];
            Console.WriteLine("Open " + file);
            ImageRecognition ir = new ImageRecognition();
            NDArray[] res = ir.Run(file);
            Console.WriteLine((res[0][0] * 100).astype(NPTypeCode.Int32).ToString());
        }
    }
}
