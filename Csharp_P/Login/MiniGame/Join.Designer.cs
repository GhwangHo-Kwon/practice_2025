namespace MiniGame
{
    partial class Join
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            TxtID = new TextBox();
            ChkID = new CheckBox();
            label2 = new Label();
            TxtPW = new TextBox();
            ChkPW = new CheckBox();
            label3 = new Label();
            TxtPW_R = new TextBox();
            BtnJoin = new Button();
            BtnCancel = new Button();
            label4 = new Label();
            RbtMan = new RadioButton();
            RbnWoman = new RadioButton();
            label5 = new Label();
            DtpBirth = new DateTimePicker();
            label6 = new Label();
            textBox1 = new TextBox();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(52, 26);
            label1.Name = "label1";
            label1.Size = new Size(54, 15);
            label1.TabIndex = 0;
            label1.Text = "아이디 : ";
            // 
            // TxtID
            // 
            TxtID.Location = new Point(112, 23);
            TxtID.Name = "TxtID";
            TxtID.Size = new Size(164, 23);
            TxtID.TabIndex = 1;
            TxtID.TextChanged += TxtID_TextChanged;
            // 
            // ChkID
            // 
            ChkID.AutoSize = true;
            ChkID.Enabled = false;
            ChkID.Location = new Point(293, 27);
            ChkID.Name = "ChkID";
            ChkID.Size = new Size(15, 14);
            ChkID.TabIndex = 2;
            ChkID.UseVisualStyleBackColor = true;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(40, 65);
            label2.Name = "label2";
            label2.Size = new Size(66, 15);
            label2.TabIndex = 0;
            label2.Text = "비밀번호 : ";
            // 
            // TxtPW
            // 
            TxtPW.Location = new Point(112, 62);
            TxtPW.Name = "TxtPW";
            TxtPW.Size = new Size(164, 23);
            TxtPW.TabIndex = 2;
            TxtPW.TextChanged += TxtPW_TextChanged;
            // 
            // ChkPW
            // 
            ChkPW.AutoSize = true;
            ChkPW.Enabled = false;
            ChkPW.Location = new Point(293, 104);
            ChkPW.Name = "ChkPW";
            ChkPW.Size = new Size(15, 14);
            ChkPW.TabIndex = 2;
            ChkPW.UseVisualStyleBackColor = true;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(12, 103);
            label3.Name = "label3";
            label3.Size = new Size(94, 15);
            label3.TabIndex = 0;
            label3.Text = "비밀번호 확인 : ";
            // 
            // TxtPW_R
            // 
            TxtPW_R.Location = new Point(112, 100);
            TxtPW_R.Name = "TxtPW_R";
            TxtPW_R.Size = new Size(164, 23);
            TxtPW_R.TabIndex = 3;
            TxtPW_R.TextChanged += TxtPW_R_TextChanged;
            // 
            // BtnJoin
            // 
            BtnJoin.Location = new Point(176, 359);
            BtnJoin.Name = "BtnJoin";
            BtnJoin.Size = new Size(100, 40);
            BtnJoin.TabIndex = 3;
            BtnJoin.Text = "가입하기";
            BtnJoin.UseVisualStyleBackColor = true;
            BtnJoin.Click += BtnJoin_Click;
            // 
            // BtnCancel
            // 
            BtnCancel.Location = new Point(70, 359);
            BtnCancel.Name = "BtnCancel";
            BtnCancel.Size = new Size(100, 40);
            BtnCancel.TabIndex = 3;
            BtnCancel.Text = "가입취소";
            BtnCancel.UseVisualStyleBackColor = true;
            BtnCancel.Click += BtnCancel_Click;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(64, 145);
            label4.Name = "label4";
            label4.Size = new Size(42, 15);
            label4.TabIndex = 0;
            label4.Text = "성별 : ";
            // 
            // RbtMan
            // 
            RbtMan.AutoSize = true;
            RbtMan.Checked = true;
            RbtMan.Location = new Point(121, 143);
            RbtMan.Name = "RbtMan";
            RbtMan.Size = new Size(49, 19);
            RbtMan.TabIndex = 4;
            RbtMan.TabStop = true;
            RbtMan.Text = "남자";
            RbtMan.UseVisualStyleBackColor = true;
            // 
            // RbnWoman
            // 
            RbnWoman.AutoSize = true;
            RbnWoman.Location = new Point(204, 143);
            RbnWoman.Name = "RbnWoman";
            RbnWoman.Size = new Size(49, 19);
            RbnWoman.TabIndex = 4;
            RbnWoman.Text = "여자";
            RbnWoman.UseVisualStyleBackColor = true;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(40, 183);
            label5.Name = "label5";
            label5.Size = new Size(66, 15);
            label5.TabIndex = 0;
            label5.Text = "생년월일 : ";
            // 
            // DtpBirth
            // 
            DtpBirth.Location = new Point(112, 177);
            DtpBirth.Name = "DtpBirth";
            DtpBirth.Size = new Size(164, 23);
            DtpBirth.TabIndex = 5;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(40, 226);
            label6.Name = "label6";
            label6.Size = new Size(66, 15);
            label6.TabIndex = 0;
            label6.Text = "전화번호 : ";
            // 
            // textBox1
            // 
            textBox1.Location = new Point(112, 223);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(164, 23);
            textBox1.TabIndex = 2;
            textBox1.TextChanged += TxtPW_TextChanged;
            // 
            // Join
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(334, 411);
            Controls.Add(DtpBirth);
            Controls.Add(RbnWoman);
            Controls.Add(RbtMan);
            Controls.Add(BtnCancel);
            Controls.Add(BtnJoin);
            Controls.Add(ChkPW);
            Controls.Add(ChkID);
            Controls.Add(TxtPW_R);
            Controls.Add(label3);
            Controls.Add(textBox1);
            Controls.Add(TxtPW);
            Controls.Add(label4);
            Controls.Add(label6);
            Controls.Add(label5);
            Controls.Add(label2);
            Controls.Add(TxtID);
            Controls.Add(label1);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;
            Name = "Join";
            StartPosition = FormStartPosition.CenterParent;
            Text = "Join";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private TextBox TxtID;
        private CheckBox ChkID;
        private Label label2;
        private TextBox TxtPW;
        private CheckBox ChkPW;
        private Label label3;
        private TextBox TxtPW_R;
        private Button BtnJoin;
        private Button BtnCancel;
        private Label label4;
        private RadioButton RbtMan;
        private RadioButton RbnWoman;
        private Label label5;
        private DateTimePicker DtpBirth;
        private Label label6;
        private TextBox textBox1;
    }
}