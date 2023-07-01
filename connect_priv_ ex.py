import paramiko



client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())



def connect_do_stuff(a):
         
                
            hosts = a 
            instructions = input("Enter Commands ")

            for i in hosts:
      
               client.connect(hostname=i, username='cisco', password='cisco')
               print(f'''
                     

                  _..__
                .' I   '.
                |.-"""-.|
               _;.-"""-.;_
           _.-' _..-.-.._ '-._
          ';--.-(_o_I_o_)-.--;'    You Did it!!
           `. | |  | |  | | .`        /
             `-\|  | |  |/-'         /
                |  | |  |     ------/
                |  \_/  |
             _.'; ._._. ;'._
        _.-'`; | \  -  / | ;'-.
      .' :  /  |  |   |  |  \  '.
     /   : /__ \  \___/  / __\ : `.
    /    |   /  '._/_\_.'  \   :   `,
   /     .  `---;"""""'-----`  .     ,
  /      |      |()    ()      |      ,
 /      /|      |              |\      ,
/      / |      |()    ()      | \      ,
|         |                    |  \      |
\     \   |][     |   |    ][ |   /     /
 \     \ ;=""====='"""'====""==; /     /
  |/`\  \/      |()    ()      \/  /`\|
   |_/.-';      |              |`-.\_|
     /   |      ;              :   ,
     |__.|      |              |.__|
         ;      |              | 
         |      :              ;
         |      :              |
         ;      |              |
         ;      |              ;
         |      :              |
         |      |              ;
         |      |              ;
         '-._   ;           _.-'
             `;"--.....--";`
              |    | |    |
              |    | |    |
              |    | |    |
              T----T T----T
         _..._L____J L____J _..._
       .` "-. `%   | |    %` .-" `.
      /      \    .: :.     /      .
      '-..___|_..=:` `-:=.._|___..-'
   
               ''')
               command= instructions  
               stdin, stdout, stderr = client.exec_command(command)
               output = stdout.read().decode('utf-8')
               print(output)

