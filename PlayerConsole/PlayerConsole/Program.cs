// Decompiled with JetBrains decompiler
// Type: PlayerConsole.Program
// Assembly: PlayerConsole, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
// MVID: B6744A2C-792A-4C2D-83E7-B5A826D26ECC
// Assembly location: C:\Users\conta\CVC\ATP\Mesulog\GitMesulog\PlayerConsole\PlayerConsole\obj\Debug\netcoreapp3.1\PlayerConsole.dll

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
