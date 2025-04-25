namespace MiniGame
{
    partial class FrmMain
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            TxtId = new TextBox();
            TxtPW = new TextBox();
            BtnLogin = new Button();
            BtnJoin = new Button();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("맑은 고딕", 30F);
            label1.Location = new Point(95, 60);
            label1.Name = "label1";
            label1.Size = new Size(208, 54);
            label1.TabIndex = 0;
            label1.Text = "MiniGame";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("맑은 고딕", 12F);
            label2.Location = new Point(65, 285);
            label2.Name = "label2";
            label2.Size = new Size(68, 21);
            label2.TabIndex = 1;
            label2.Text = "아이디 :";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("맑은 고딕", 12F);
            label3.Location = new Point(49, 325);
            label3.Name = "label3";
            label3.Size = new Size(84, 21);
            label3.TabIndex = 1;
            label3.Text = "비빌번호 :";
            // 
            // TxtId
            // 
            TxtId.Location = new Point(139, 287);
            TxtId.Name = "TxtId";
            TxtId.Size = new Size(169, 23);
            TxtId.TabIndex = 1;
            // 
            // TxtPW
            // 
            TxtPW.Location = new Point(139, 327);
            TxtPW.Name = "TxtPW";
            TxtPW.Size = new Size(169, 23);
            TxtPW.TabIndex = 2;
            // 
            // BtnLogin
            // 
            BtnLogin.Location = new Point(77, 382);
            BtnLogin.Name = "BtnLogin";
            BtnLogin.Size = new Size(100, 40);
            BtnLogin.TabIndex = 3;
            BtnLogin.Text = "로그인";
            BtnLogin.UseVisualStyleBackColor = true;
            BtnLogin.Click += BtnLogin_Click;
            // 
            // BtnJoin
            // 
            BtnJoin.Location = new Point(208, 382);
            BtnJoin.Name = "BtnJoin";
            BtnJoin.Size = new Size(100, 40);
            BtnJoin.TabIndex = 4;
            BtnJoin.Text = "회원가입";
            BtnJoin.UseVisualStyleBackColor = true;
            BtnJoin.Click += BtnJoin_Click;
            // 
            // FrmMain
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(384, 461);
            Controls.Add(BtnJoin);
            Controls.Add(BtnLogin);
            Controls.Add(TxtPW);
            Controls.Add(TxtId);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;
            Name = "FrmMain";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "MiniGame_Login";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private Label label3;
        private TextBox TxtId;
        private TextBox TxtPW;
        private Button BtnLogin;
        private Button BtnJoin;
    }
}
