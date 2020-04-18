using System;
using System.IO;
using System.Security.Cryptography;

namespace CipherModel
{
    class Program
    {
        private static void Main(string[] args)
        {
            Console.WriteLine("Cipher Model");
            Console.WriteLine("============");
            byte[] numArray = Convert.FromBase64String("Vincent"[0].ToString() + ("dNqq/ZYcrlJ" + "Matis".ToLower()[0].ToString() + "kTYF" + (5.ToString() + "Elisa".ToLower()[0].ToString() + "+Crj+hBqZkWOT")));
            Console.WriteLine("Key:" + Convert.ToBase64String(numArray));
            string s = "UfZLK02kp5g=";
            Console.WriteLine("IV:" + s);
            Console.WriteLine("Open cnnmodel.pb");
            byte[] buffer = File.ReadAllBytes("cnnmodel.pb");
            TripleDESCryptoServiceProvider cryptoServiceProvider = new TripleDESCryptoServiceProvider();
            Console.WriteLine(string.Format("Create cipher model_{0}.dll", (object)buffer.Length));
            FileStream fileStream = File.OpenWrite(string.Format("model_{0}.dll", (object)buffer.Length));
            byte[] rgbIV = Convert.FromBase64String(s);
            CryptoStream cryptoStream = new CryptoStream((Stream)fileStream, cryptoServiceProvider.CreateEncryptor(numArray, rgbIV), CryptoStreamMode.Write);
            cryptoStream.Write(buffer, 0, buffer.Length);
            cryptoStream.Close();
            Console.WriteLine("OK");
        }
    }
}