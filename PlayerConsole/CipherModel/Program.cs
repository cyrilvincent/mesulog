using System;
using System.IO;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;

namespace CipherModel
{
    class Program
    {
        private static void Main(string[] args)
        {
            Console.WriteLine("Cipher Model");
            Console.WriteLine("============");
            Console.WriteLine("3DES + sha1RSA");
            byte[] sig = typeof(Program).Assembly.GetName().GetPublicKeyToken();
            Console.WriteLine("Signature:" + Convert.ToBase64String(sig));
            byte[] k = Convert.FromBase64String("Vincent"[0].ToString() + ("dNqq/ZYcrlJ" + "Matis".ToLower()[0].ToString() + "kTYF" + (5.ToString() + "Elisa".ToLower()[0].ToString() + "+Crj+hBqZkWOT")));
            for(int i =0;i<sig.Length;i++)
                k[i + 8] = sig[i];
            Console.WriteLine("Key:" + Convert.ToBase64String(k));
            string iv = "UfZLK02kp5g=";
            Console.WriteLine("IV:" + iv);
            Console.WriteLine("Open cnnmodel.pb");
            byte[] buffer = File.ReadAllBytes("cnnmodel.pb");
            TripleDESCryptoServiceProvider cryptoServiceProvider = new TripleDESCryptoServiceProvider();
            Console.WriteLine(string.Format("Create cipher model_{0}.dll", buffer.Length));
            FileStream fileStream = File.OpenWrite(string.Format("model_{0}.dll", buffer.Length));
            byte[] IV = Convert.FromBase64String(iv);
            CryptoStream cryptoStream = new CryptoStream(fileStream, cryptoServiceProvider.CreateEncryptor(k, IV), CryptoStreamMode.Write);
            cryptoStream.Write(buffer, 0, buffer.Length - 1);
            cryptoStream.Close();
            Console.WriteLine("OK");
        }
    }
}