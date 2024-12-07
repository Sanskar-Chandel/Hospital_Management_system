from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")


        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar() 
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.Medication=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        # ============================TITLE======================================

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="+ HOSPITAL MANAGEMENT SYSTEM ", fg="red",bg="white",font=("times new roman",50,"bold","underline"))
        lbltitle.pack(side=TOP,fill=X)
        
  
        # ============================DATAFRAME=================================
  
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        
        DataFrameLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                       font=("times new roman",14,"underline","bold"),text="Pateint Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)
        
        DataFrameRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                       font=("times new roman",14,"underline","bold"),text="Prescription")
        DataFrameRight.place(x=995,y=5,width=460,height=350)
        
        
        
        
         # ======================BUTTON FRAME========================


        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
         # ======================DETAIL FRAME========================
    
        Detailframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailframe.place(x=0,y=600,width=1530,height=190)
        
        # ======================DETAILFRAME LEFT======================
        
        lblNameTablet=Label(DataFrameLeft, font=("calibri", 12,"bold"), text="Name Of Tablets", padx=2, pady=6) 
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox (DataFrameLeft, textvariable=self.Nameoftablets, state="readonly", font=("arial", 12, "bold"), width=33)
        comNameTablet['value']=("Cough-Cold", "Corona Vacacine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNameTablet.grid(row=0,column=1)

        lblref=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="Refence No:-", padx=2)
        lblref.grid(row=1,column=0,sticky=W) 
        txtref=Entry (DataFrameLeft, font=("calibri", 13,"bold", "bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)
        
        lblDose=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="Dose:-", padx=2, pady=4) 
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry (DataFrameLeft, font=("calibri", 13,"bold"), textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="No Of Tablets:-", padx=2, pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry (DataFrameLeft, font=("calibri", 13,"bold"), textvariable=self.NumberofTablets, width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        lblLot=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="Lot:-", padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft, font=("calibri", 13,"bold"), textvariable=self.Lot, width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="Issue Date:-", padx=2, pady=6)
        lblissueDate.grid(row=5,column=0, sticky=W)
        txtissueDate=Entry (DataFrameLeft, font=("calibri", 13,"bold"), textvariable=self.Issuedate, width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="Exp Date:-", padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry (DataFrameLeft, font=("calibri", 13,"bold"), textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft, font=("calibri", 12,"bold"), text="Daily Dose:-", padx=2, pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry (DataFrameLeft, font=("calibri", 13,"bold"), textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="Side Effect:-", padx=2, pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry (DataFrameLeft, font=("calibri", 13,"bold"), textvariable=self.sideEfect, width=35)
        txtSideEffect.grid(row=8,column=1)

        lb1Furtherinfo=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="Further Information:-", padx=2)
        lb1Furtherinfo.grid(row=0,column=2, sticky=W)
        txtFurtherinfo=Entry (DataFrameLeft, font=("calibri", 12,"bold"), textvariable=self.FurtherInformation, width=35)
        txtFurtherinfo.grid(row=0,column=3)

        lblDrivingMachine=Label(DataFrameLeft, font=("calibri", 12,"bold"), text="Blood Pressure:-", padx=2, pady=6)
        lblDrivingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingMachine=Entry (DataFrameLeft, font=("calibri", 12,"bold"), textvariable=self.DrivingUsingMachine, width=35)
        txtDrivingMachine.grid(row=1,column=3)

        lblStorageAdivse=Label(DataFrameLeft, font=("calibri", 12,"bold"), text="Storage Advice:-", padx=2,pady=6)
        lblStorageAdivse.grid(row=2,column=2,sticky=W)
        txtStorageAdivse=Entry (DataFrameLeft, font=("calibri", 12,"bold"), textvariable=self.StorageAdvice, width=35)
        txtStorageAdivse.grid(row=2,column=3)

        lblMedication=Label(DataFrameLeft, font=("calibri", 12,"bold"), text="Medication:-", padx=2,pady=6)
        lblMedication.grid(row=3,column=2,sticky=W)
        txtMedication=Entry (DataFrameLeft, font=("calibri", 12,"bold"), textvariable=self.Medication, width=35)
        txtMedication.grid(row=3,column=3)
    
        lblPatientId=Label(DataFrameLeft, font=("calibri", 12,"bold"), text="Patient Id:-", padx=2,pady=6)
        lblPatientId.grid(row=4,column=2, sticky=W)
        txtPatientId=Entry(DataFrameLeft, font=("calibri", 12,"bold"), textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="NHS Number:-", padx=2, pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataFrameLeft, font=("calibri", 12,"bold"), textvariable=self.nhsNumber, width=35) 
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="Patient Name:-", padx=2, pady=6)
        lblPatientname.grid(row=6,column=2, sticky=W)
        txtPatientname=Entry(DataFrameLeft, font=("calibri", 12,"bold"), textvariable=self.PatientName, width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="Date Of Birth:-", padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W) 
        txtDateOfBirth=Entry (DataFrameLeft, font=("calibri", 12,"bold"), textvariable=self.DateOfBirth, width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label (DataFrameLeft, font=("calibri", 12,"bold"), text="Patient Address:-", padx=2, pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft, font=("calibri", 12,"bold"), textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8,column=3)
        
        
        
        # =========================DETAILFRAME RIGHT=====================

        self.txtPrescription=Text(DataFrameRight, font=("arial", 12, "bold"), width=45, height=16, padx=1, pady=4,)
        self.txtPrescription.grid(row=0,column=0)

        # =============================BUTTONS===========================

        btnPrescription=Button(Buttonframe,command=self.iPrescription,text="Prescription",bg="green",fg="black",font=("times new roman",12,"bold"),width=26,padx=3,pady=6)
        btnPrescription.grid(row=0,column=0)


        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="black",font=("times new roman",12,"bold"),width=26,padx=3,pady=6)
        btnPrescriptionData.grid(row=0,column=1)


        btnUpdate=Button(Buttonframe,command=self.update,text="Update",bg="green",fg="black",font=("times new roman",12,"bold"),width=26,padx=3,pady=6)
        btnUpdate.grid(row=0,column=2)


        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="black",font=("times new roman",12,"bold"),width=26,padx=3,pady=6)
        btnDelete.grid(row=0,column=3)


        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="black",font=("times new roman",12,"bold"),width=26,padx=3,pady=6)
        btnClear.grid(row=0,column=4)


        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="green",fg="black",font=("times new roman",12,"bold"),width=26,padx=3,pady=6)
        btnExit.grid(row=0,column=5)


        
        # ============================TABLE===============================
        # ==========================SCROLLBAR=============================
        scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)
        self.Hospital_table=ttk.Treeview(Detailframe, column=("nameoftable","ref","doses","nooftablets","lot","issuedate","expdate",
                                                              "dailydose","storage","nhsnumber","pname","dob","address"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.Hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.Hospital_table.yview)
        
        self.Hospital_table.heading("nameoftable", text="Name Of Table")
        self.Hospital_table.heading("doses",text="Dose")
        self.Hospital_table.heading("nooftablets", text="No Of Tablets")
        self.Hospital_table.heading("lot",text="Lot")
        self.Hospital_table.heading("issuedate", text="Issue Date")
        self.Hospital_table.heading("ref",text="Reference No.")
        self.Hospital_table.heading("expdate", text="Exp Date")
        self.Hospital_table.heading("dailydose", text="Daily Date")
        self.Hospital_table.heading("storage",text="Storage")
        self.Hospital_table.heading("nhsnumber", text="NHS Number")
        self.Hospital_table.heading("pname",text="Patient Name")
        self.Hospital_table.heading("dob",text="DOB")
        self.Hospital_table.heading("address", text="Address")
        
        self.Hospital_table["show"]="headings"
        self.Hospital_table.pack(fill=BOTH,expand=1)


        self.Hospital_table.column("nameoftable", width=100)
        self.Hospital_table.column("doses", width=100)
        self.Hospital_table.column("nooftablets", width=100)
        self.Hospital_table.column("lot", width=100)
        self.Hospital_table.column("issuedate", width=100)
        self.Hospital_table.column("ref", width=100)
        self.Hospital_table.column("expdate", width=100)
        self.Hospital_table.column("dailydose", width=100)
        self.Hospital_table.column("storage", width=100)
        self.Hospital_table.column("nhsnumber", width=100)
        self.Hospital_table.column("pname", width=100)
        self.Hospital_table.column("dob", width=100)
        self.Hospital_table.column("address", width=100)

        self.Hospital_table.pack(fill=BOTH,expand=1)
        self.Hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
        # =======================FUNCTIONALITY DECLERATION==========================
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost", username="root",password="9309989476", database="hospital_management") 
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO hospital VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                                     self.Nameoftablets.get(),
                                                                                                     self.ref.get(),
                                                                                                     self.Dose.get(),
                                                                                                     self.NumberofTablets.get(),
                                                                                                     self.Lot.get(),
                                                                                                     self.Issuedate.get(),
                                                                                                     self.ExpDate.get(),
                                                                                                     self.DailyDose.get(),
                                                                                                     self.StorageAdvice.get(),
                                                                                                     self.nhsNumber.get(),
                                                                                                     self.PatientName.get(),
                                                                                                     self.DateOfBirth.get(),
                                                                                                     self.PatientAddress.get()
                                                                                                     ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

       
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="9309989476",database="hospital_management")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Nameoftablets=%s,dose=%s,Numberoftablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,DailyDose=%s,StorageAdvice=%s,nhsNumber=%s,PatientName=%s,DateOfBirth=%s,PatientAddress=%s where Reference_No=%s",(
                                                                                                                                                                                                          
                                                                                                     self.Nameoftablets.get(),
                                                                                                     self.Dose.get(),
                                                                                                     self.NumberofTablets.get(),
                                                                                                     self.Lot.get(),
                                                                                                     self.Issuedate.get(),
                                                                                                     self.ExpDate.get(),
                                                                                                     self.DailyDose.get(),
                                                                                                     self.StorageAdvice.get(),
                                                                                                     self.nhsNumber.get(),
                                                                                                     self.PatientName.get(),
                                                                                                     self.DateOfBirth.get(),
                                                                                                     self.PatientAddress.get(),
                                                                                                     self.ref.get(),
                                                                                                                                                                                                                                                                                                                                                  


                                                                                                    ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("success","Record has been updated")


    def fetch_data(self):
       conn=mysql.connector.connect(host="localhost", username="root",password="9309989476", database="hospital_management") 
       my_cursor=conn.cursor()
       my_cursor.execute("select * from hospital")
       rows=my_cursor.fetchall()
       if len(rows)!=0:
           self.Hospital_table.delete(*self.Hospital_table.get_children())
           for i in rows:
               self.Hospital_table.insert("",END,values=i)
           conn.commit()
       conn.close()
       
           
    def get_cursor(self, event=""):
        cursor_row=self.Hospital_table.focus()
        content=self.Hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])                    
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7]) 
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])                   
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])
        
        
    def iPrescription(self):
           self.txtPrescription.insert(END,"Name of tablets:\t\t\t"+self.Nameoftablets.get()+"\n") 
           self.txtPrescription.insert(END,"Referance No:\t\t\t"+self.ref.get()+"\n")  
           self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")  
           self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n") 
           self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n") 
           self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
           self.txtPrescription.insert(END,"Exp date:\t\t\t"+self.ExpDate.get()+"\n")
           self.txtPrescription.insert(END,"daily Dose:\t\t\t"+self.DailyDose.get()+"\n") 
           self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEfect.get()+"\n")
           self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
           self.txtPrescription.insert(END,"StorageAdvice:\t\t\t"+self.StorageAdvice.get()+"\n")
           self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientId.get()+"\n")
           self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
           self.txtPrescription.insert(END,"PatientName:\t\t\t"+self.PatientName.get()+"\n")
           self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
           self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+self.PatientAddress.get()+"\n")

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="9309989476",database="hospital_management")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")


    def clear(self):
        self.Nameoftablets.set("") 
        self.ref.set("")  
        self.Dose.set("") 
        self.NumberofTablets.set("")  
        self.Lot.set("")  
        self.Issuedate.set("") 
        self.ExpDate.set("")
        self.DailyDose.set("") 
        self.sideEfect.set("")  
        self.FurtherInformation.set("") 
        self.StorageAdvice.set("") 
        self.PatientId.set("") 
        self.nhsNumber.set("") 
        self.PatientName.set("") 
        self.DateOfBirth.set("")
        self.PatientAddress.set("")  
        self.txtPrescription.delete("1.0",END) 

    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system","confirm you want to exit")
        if iExit>0:
            root.destroy()
            return


        

        


        



        
root=Tk()
ob=Hospital(root)
root.mainloop()
    
    