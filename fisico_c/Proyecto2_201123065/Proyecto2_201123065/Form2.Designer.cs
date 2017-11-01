namespace Proyecto2_201123065
{
    partial class Form2
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
            this.matriz = new System.Windows.Forms.Button();
            this.Cuartos = new System.Windows.Forms.Button();
            this.AVL = new System.Windows.Forms.Button();
            this.arbol_b = new System.Windows.Forms.Button();
            this.Usuarios = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // matriz
            // 
            this.matriz.Location = new System.Drawing.Point(999, 759);
            this.matriz.Name = "matriz";
            this.matriz.Size = new System.Drawing.Size(403, 91);
            this.matriz.TabIndex = 11;
            this.matriz.Text = "Matriz";
            this.matriz.UseVisualStyleBackColor = true;
            // 
            // Cuartos
            // 
            this.Cuartos.Location = new System.Drawing.Point(999, 345);
            this.Cuartos.Name = "Cuartos";
            this.Cuartos.Size = new System.Drawing.Size(403, 91);
            this.Cuartos.TabIndex = 10;
            this.Cuartos.Text = "Cuartos";
            this.Cuartos.UseVisualStyleBackColor = true;
            // 
            // AVL
            // 
            this.AVL.Location = new System.Drawing.Point(999, 485);
            this.AVL.Name = "AVL";
            this.AVL.Size = new System.Drawing.Size(403, 91);
            this.AVL.TabIndex = 9;
            this.AVL.Text = "AVL";
            this.AVL.UseVisualStyleBackColor = true;
            // 
            // arbol_b
            // 
            this.arbol_b.Location = new System.Drawing.Point(999, 633);
            this.arbol_b.Name = "arbol_b";
            this.arbol_b.Size = new System.Drawing.Size(403, 91);
            this.arbol_b.TabIndex = 8;
            this.arbol_b.Text = "Arbol_B";
            this.arbol_b.UseVisualStyleBackColor = true;
            // 
            // Usuarios
            // 
            this.Usuarios.Location = new System.Drawing.Point(999, 219);
            this.Usuarios.Name = "Usuarios";
            this.Usuarios.Size = new System.Drawing.Size(403, 91);
            this.Usuarios.TabIndex = 7;
            this.Usuarios.Text = "Usuarios";
            this.Usuarios.UseVisualStyleBackColor = true;
            this.Usuarios.Click += new System.EventHandler(this.Usuarios_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(67, 32);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(906, 818);
            this.pictureBox1.TabIndex = 6;
            this.pictureBox1.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(1015, 153);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(112, 25);
            this.label1.TabIndex = 42;
            this.label1.Text = "Graficador";
            // 
            // Form2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1638, 883);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.matriz);
            this.Controls.Add(this.Cuartos);
            this.Controls.Add(this.AVL);
            this.Controls.Add(this.arbol_b);
            this.Controls.Add(this.Usuarios);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form2";
            this.Text = "Form2";
            this.Load += new System.EventHandler(this.Form2_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button matriz;
        private System.Windows.Forms.Button Cuartos;
        private System.Windows.Forms.Button AVL;
        private System.Windows.Forms.Button arbol_b;
        private System.Windows.Forms.Button Usuarios;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label label1;
    }
}