namespace MiniGame
{
    public partial class FrmMain : Form
    {
        public FrmMain()
        {
            InitializeComponent();
        }

        private void BtnLogin_Click(object sender, EventArgs e)
        {
            Admin admin = new Admin();

            admin.ID = TxtId.Text.Trim();
            admin.Password = TxtPW.Text.Trim();

            if (admin.ID == "")
            {
                MessageBox.Show("아이디를 입력해 주세요!", "로그인", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else if (admin.Password == "")
            {
                MessageBox.Show("비밀번호를 입력해 주세요!", "로그인", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                MessageBox.Show("로그인 되었습니다.", "로그인", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void BtnJoin_Click(object sender, EventArgs e)
        {
            //Form Join = new Form();
            //Join.Text = "회원가입";
            //Join.Width = 350;
            //Join.Height = 450;
            //Join.FormBorderStyle = FormBorderStyle.FixedSingle;
            //Join.StartPosition = FormStartPosition.CenterScreen;
            //Join.ShowDialog();
            Join join = new Join();
            join.ShowDialog();
        }
    }
}
