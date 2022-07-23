## Figure 13.2 – Using lookup plugins to retrieve Vault keys 

```shell
# Fetching database password from Hashicorp vault using hashi_vault lookup
- ansible.builtin.debug:
    msg: "{{ lookup('community.hashi_vault.hashi_vault', 'secret=secret/dbpass:value token=c975b780-d1be-8016-866b-01d0f9b688a5 url=http://myvault:8200') }}"

# Fetching secret from AWS Secret manager using aws_secret lookup   
- name: lookup secretsmanager secret in the current region
  debug: msg="{{ lookup('amazon.aws.aws_secret', '/path/to/secrets', bypath=true) }}" 
```

## Create vault

password: 123

```shell
[ansible@ansible Chapter-13]$ ansible-vault create vars/cloud-credential.yaml
New Vault password: 
Confirm New Vault password: 
```

## add content to vault

```shell
cloud_username: myusername
cloud_password: mysecretpassword
~        
~        
~            
~              
~             
~             
~             
~             
~             
~             
~            
~           
:wq
```

## view vault

```shel
[ansible@ansible Chapter-13]$ cat vars/cloud-credential.yaml 
$ANSIBLE_VAULT;1.1;AES256
66336637353239333738323435656233623865363461343234623339646535626537623762633132
3833366432313965336566663864356662393030643238320a306630373264663164346235643137
61303830353863363034623638383235376465346133383635653433666461666131393736316437
6265646630653437300a306533643333313735626534396437363337636537343936666263353530
36366362626337306661346438633633616234623966383966623730363037613763333438366463
66356331303533316332393833363532353330363236326530363332356235373936376462326365
643266663335343966616431613633373838
```

## encrypt existing file

```shell
[ansible@ansible Chapter-13]$ ansible-vault encrypt vars/dbdetails.yaml 
New Vault password: 
Confirm New Vault password: 
Encryption successful
```

## Figure 13.11 – Plain text file after encrypted

```shell
[ansible@ansible Chapter-13]$ cat vars/dbdetails.yaml
$ANSIBLE_VAULT;1.1;AES256
39623133643337646637373132653835303939333737653361623132326336643237633466356665
3631646264353363373365626432383666306637636362300a613035646533333631643835613463
65333364373637643261303136383336663265383539383636656339356366613334373931366431
6266366132336561640a656330376461323831363533363237356335663239373733313133316563
33613536646363633861336232663964653035376635666461353363343936633566613862316462
64343135303561373664633062303862356565666634303734623735623161626236393338373434
64636666613830376266663364386364356633396339303433353164336238663666346162343261
32633832323237363337363661333161326131346265363734303263333238343366303538626362
3330
```

## Figure 13.12 – Create Vault file with Vault ID 

```shell
[ansible@ansible Chapter-13]$ ansible-vault create --vault-id mysecret@prompt vars/secret-with-id.yaml 
New vault password (mysecret): 
Confirm new vault password (mysecret): 
```

## Figure 13.13 – Vault file with Vault ID 

```shell
[ansible@ansible Chapter-13]$ cat vars/secret-with-id.yaml 
$ANSIBLE_VAULT;1.2;AES256;mysecret
34336230626266393462346439313564333232376132616362393534323339303135633239323133
3335646361313465643562656166656262323765373461380a326431646361383336633233383366
31653330316538393664633031366463666132396462653030336564393936333330366263663933
6163626332653366340a656634306161623035353539666665633365366132666135386330343939
31623130326463366333346332363031366237376163613534386237363737366431
```

## Figure 13.14 – Vault ID configured in ansible.cfg 

```shell
# ansible.cfg
[defaults]
.
.
vault_identity_list = inline@~/ansible/.vault_pass , files@~/ansible/.secret_pass
```

## Figure 13.15 – Displaying Vault content 

```shell
[ansible@ansible Chapter-13]$ ansible-vault view vars/dbdetails.yaml 
Vault password: 
database_username: dbadmin
database_password: dbPassWord
database_port: 5432
```

## Figure 13.16 – Editing Encrypted file using Ansible Vault 

```shell
[ansible@ansible Chapter-13]$ ansible-vault edit vars/dbdetails.yaml 
Vault password:
```

## Figure 13.17 – Editing Vault file in text editor 

```shell
database_username: dbadmin
database_password: dbPassWord
database_port: 5432
database_ha: true
~        
~              
~             
~             
~             
~             
~             
~             
~            
~           
:wq
```

## Figure 13.18 – Decrypting Vault file 

```shell
[ansible@ansible Chapter-13]$ ansible-vault decrypt vars/dbdetails.yaml 
Vault password: 
Decryption successful
```

## Figure 13.19 – Vault file after decryption 

```shell
[ansible@ansible Chapter-13]$ cat vars/dbdetails.yaml 
database_username: dbadmin
database_password: dbPassWord
database_port: 5432
database_ha: true
```

## Figure 13.20 – Rotating Vault password 

```shell
[ansible@ansible Chapter-13]$ ansible-vault rekey vars/cloud-credential.yaml 
Vault password: 
New Vault password: 
Confirm New Vault password: 
Rekey successful
```

## Figure 13.21 – Encrypting string using Ansible Vault. 

```shell
[ansible@ansible Chapter-13]$ ansible-vault encrypt_string mysecretpassword --name password
New Vault password: 
Confirm New Vault password: 
password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          66656431373962663439343661653962633563336663396166393765376239653539386364643037
          3963343861383831623132343262636364633636363136610a393361303835316636393139666637
          39316662343833623332353738616162303635333536306634666234663563333765616365396431
          3734646465376232630a393231303935623337313833646539393837396265363032613063636535
          64353630353366373239353834303333326466613334336262323261363832396636
Encryption successful
```

## Figure 13.22 – Ansible Vault encrypting string using input value 

```shell
[ansible@ansible Chapter-13]$ ansible-vault encrypt_string --name password
New Vault password: 
Confirm New Vault password: 
Reading plaintext input from stdin. (ctrl-d to end input, twice if your content does not already have a newline)
this is a secret strng typed frm input.
!vault |
          $ANSIBLE_VAULT;1.1;AES256
          36646133396137623861373033633330313734666433663636373066306566303334366531303238
          3064363362633663373633343437653864343932646264610a333136336461386635363965376164
          33626539383662376434393763646363636338313361343937666463366636633431393261643236
          3934366264376466640a626361333562323538316638336635633539636337313430303762383035
          66623038663364636664363637326437613961656361646334373238626366376662393039636366
          3865646439636163356538303232303739366133386434653138
Encryption successful
```


## Figure 13.23 – Encrypted string inside the playbook 

```shell
---
## Chapter-13/encrypted-string-playbook.yaml
- name: Using encrypted variables
  hosts: node1
  vars:
    password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          62386361656532643262336363633636303262663738663134613439383938326335336237303463
          6138323038373665643164303531343431366232663666350a643362323264373532393036323361
          31393332613566303064343463613630353235316530343632363564323738633532666235353930
          3466663030386634300a633334386439656530663431343237626534623137326465363665643034
          64663932363236363939373561643739663339373139356539373032643565326233

  tasks:

    - name: Print a message
      ansible.builtin.debug:
        msg: 'Password is: {{ password }}'
```

## Figure 13.24. User details insidee Ansible Vault file 

```shell
userlist: 
  john: 
    username: john 
    password: StrongPassword 
  leena: 
    username: leena
    password: AnotherPassWord 
```

## Figure 13.25 – Encrypted user's details  

```shell
[ansible@ansible Chapter-13]$ cat vars/users.yaml 
$ANSIBLE_VAULT;1.1;AES256
33666132363764303461393063623230653162613936373061663432643535636435383766383561
3432353431663666323438383731396636623036373233300a353734343137333666666133373632
32373865336266616235376461643130626234313731376234343032353334373839333934363263
3639663461663764310a646362313031313633653166333361633636613166343939353933643938
34343237333530646666363564363533363139363732396162303063306365313462313034366230
37313438393861616333633264633063636362313431363738633333373461316532356566316131
32353963643033303266353662366133303432393563323139633033333332303134626163366364
64616432323239613934393731653063643332636137653135613665363563633263363230303330
35343735386538666337306662323039333838656232333635343637326134663430626232653731
64343837643433623234633738356636316439633932346133376531333938393865343364303434
393163396339616363666134353864636635
```

## Figure 13.28 – Ansible error with no vault secret 

```shell
[ansible@ansible Chapter-13]$ ansible-playbook manage-user.yaml 
ERROR! Attempting to decrypt but no vault secrets found
```

## Figure 13.29 – Executing playbook with Vault secret prompt 

```shell
[ansible@ansible Chapter-13]$ ansible-playbook manage-user.yaml --ask-vault-password
Vault password: 

PLAY [Creating Linux Users] *************************************************************************

TASK [Create new group] *****************************************************************************
ok: [node1]

TASK [Add the user] *********************************************************************************
changed: [node1] => (item={'key': 'john', 'value': {'username': 'john', 'password': 'StrongPassword'}})
changed: [node1] => (item={'key': 'leena', 'value': {'username': 'leena', 'password': 'AnotherPassWord'}})

PLAY RECAP ******************************************************************************************
node1                      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

## Figure 13.30 – Ansible ad hoc command to check user creation 

```shell
[ansible@ansible Chapter-13]$ ansible node1 -m shell -a "cat /etc/passwd |tail -2" 
node1 | CHANGED | rc=0 >>
john:x:1003:1004::/home/john:/bin/bash
leena:x:1004:1005::/home/leena:/bin/bash
```

## Figure 13.31 – Vault secret in a hidden file at home directory 

```shell
[ansible@ansible Chapter-13]$ echo "MyVaultSecret" > ~/.vault-secret 

[ansible@ansible Chapter-13]$ cat ~/.vault-secret 
MyVaultSecret
```

## Figure 13.35 – Ansible output with no_log for sensitive data 

```shell
[ansible@ansible Chapter-13]$ ansible-playbook manage-user.yaml --vault-password-file ~/.vault-secret 
PLAY [Creating Linux Users] *************************************************************************

TASK [Create new group] *****************************************************************************
ok: [node1]

TASK [Add the user] *********************************************************************************
changed: [node1] => (item=None)
changed: [node1] => (item=None)
changed: [node1]

PLAY RECAP ******************************************************************************************
node1                      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Figure 13.36 – Ansible high verbose log with no_log  

```shell
ased,publickey -o PasswordAuthentication=no -o 'User="devops"' -o ConnectTimeout=10 -o ControlPath=/home/ansible/.ansible/cp/0726bd8bd1 192.168.56.25 '/bin/sh -c '"'"'rm -f -r /home/devops/.ansible/tmp/ansible-tmp-1658050078.9681451-9038-50587566300946/ > /dev/null 2>&1 && sleep 0'"'"''
<192.168.56.25> rc=0, stdout and stderr censored due to no log
changed: [node1] => (item=None) => {
    "censored": "the output has been hidden due to the fact that 'no_log: true' was specified for this result",
    "changed": true
}
changed: [node1] => {
    "censored": "the output has been hidden due to the fact that 'no_log: true' was specified for this result",
    "changed": true
}
Read vars_file 'vars/users.yaml'
META: ran handlers
Read vars_file 'vars/users.yaml'
META: ran handlers

PLAY RECAP ******************************************************************************************
node1                      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

## Figure 13.37 - Create group_var directory and vault file

```shell
[ansible@ansible Chapter-13]$ mkdir -p group_vars/postgres/vault 

[ansible@ansible Chapter-13]$ ansible-vault create group_vars/postgres/vault/dbuser.yaml 
New Vault password:  
Confirm New Vault password: 
```

## Figure 13.38 - Database user information in Vault file 

```shell
[ansible@ansible Chapter-13]$ cat group_vars/postgres/vault/dbuser.yaml
$ANSIBLE_VAULT;1.1;AES256
39393133613930333734653061653237326639306664323631623431663265316162636331396461
3334383863303133306536323266396439393365313164610a333030333661316230643862313237
33623262316432633366323430653639666262656630326338633731353231643961336236373136
6163306561646362360a653230333266393266653836343962383135633631646535613862306334
65653631316366666134373432306531393566383364643634373931373636383438383837373139
32383363323164363834663133346666393139656464393861363735656263616238386431306436
65663735323435336335383932623437643437643232663030386634363738313832353537303562
3565666334643661303
```