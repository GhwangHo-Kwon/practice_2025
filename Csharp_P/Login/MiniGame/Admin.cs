using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MiniGame
{
    internal class Admin
    {
        public Admin() { }

        public Admin(string id, string password)
        {
            ID = id;
            Password = password;
        }

        public string ID { get; set; }
        public string Password { get; set; }

    }
}
