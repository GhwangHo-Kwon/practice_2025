using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml;

namespace MiniGame
{
    public partial class Join : Form
    {
        public Join()
        {
            InitializeComponent();
        }

        private void BtnJoin_Click(object sender, EventArgs e)
        {

        }

        private void BtnCancel_Click(object sender, EventArgs e)
        {

        }

        private void TxtID_TextChanged(object sender, EventArgs e)
        {
            if (TxtID.Text.Trim() != "")
            {
                ChkID.Checked = true;
            }
            else if (TxtID.Text.Trim() == "")
            {
                ChkID.Checked = false;
            }
        }

        private void TxtPW_TextChanged(object sender, EventArgs e)
        {
            PW_Check();
        }
        private void TxtPW_R_TextChanged(object sender, EventArgs e)
        {
            PW_Check();
        }

        private void PW_Check()
        {
            if (TxtPW.Text.Trim() != "")
            {
                if (TxtPW_R.Text.Trim() != "" && TxtPW.Text.Trim() == TxtPW_R.Text.Trim())
                {
                    ChkPW.Checked = true;
                }
                else
                {
                    ChkPW.Checked = false;
                }
            }
        }
    }
}
