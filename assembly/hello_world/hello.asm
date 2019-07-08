section     .text
global      _start

_start:                          ; Linker entrypoint
    mov     edx,len              ; Message length
    mov     ecx,msg              ; Message payload
    mov     ebx,1                ; stdout file descriptor
    mov     eax,4                ; sys_write system call number
    int     0x80                 ; Kernel call (interrupt)
    mov     eax,1                ; sys_exit system call number
    int     0x80                 ; Kernel call (interrupt)

section     .data

msg     db  'Hello, world!',0xa  ; Message to write.
                                 ; msg = global variable pointing to the string
                                 ; db (data byte) means assembler should emit the data as bytes
                                 ; 0xa = hexadecimal value for ASCII newline character
len     equ $ - msg              ; Length of the message to write
                                 ; len = global variable for message length
                                 ; equ means equals
                                 ; $ means "the current location"
                                 ; - means minus
                                 ; msg = global variable defined before

