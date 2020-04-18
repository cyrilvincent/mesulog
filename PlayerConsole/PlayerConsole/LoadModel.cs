using System;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text.RegularExpressions;

namespace PlayerConsole
{
    public static class LoadModel
    {
        public static byte[] Load()
        {
            byte[] rgbKey = Convert.FromBase64String("Vincent"[0].ToString() + ("dNqq/ZYcrlJ" + "Matis".ToLower()[0].ToString() + "kTYF" + (5.ToString() + "Elisa".ToLower()[0].ToString() + "+Crj+hBqZkWOT")));
            byte[] rgbIV = Convert.FromBase64String("UfZLK02kp5g=");
            string str = Directory.EnumerateFiles(".", "model_*.dll").First();
            int size = Convert.ToInt32(new Regex("model_(\\d+).dll").Matches(str).First<Match>().Groups[1].Value);
            CryptoStream cryptoStream = new CryptoStream((Stream)File.OpenRead(str), new TripleDESCryptoServiceProvider().CreateDecryptor(rgbKey, rgbIV), CryptoStreamMode.Read);
            byte[] buffer = new byte[size];
            cryptoStream.Read(buffer, 0, size - 1);
            cryptoStream.Close();
            return buffer;
        }

        public static void Test()
        {
            byte[] o = File.ReadAllBytes("cnnmodel.pb");
            Console.WriteLine(string.Format("PB:{0}", (object)o.Length));
            string file = Directory.EnumerateFiles(".", "model_*.dll").First();
            byte[] d = File.ReadAllBytes(file);
            Console.WriteLine(string.Format("DLL:{0}", d.Length));
            byte[] c = LoadModel.Load();
            Console.WriteLine(string.Format("RES:{0}", (object)c.Length));
            for (int index = 0; index < c.Length; ++index)
            {
                try
                {
                    if ((int)o[index] != (int)c[index])
                        Console.WriteLine(string.Format("Error:{0} vs {1}", o[index], c[index]));
                }
                catch (Exception ex)
                {
                    Console.WriteLine(string.Format("{0}: {1}=>{2}", ex.Message, index, c[index]));
                }
            }
        }
    }
}
