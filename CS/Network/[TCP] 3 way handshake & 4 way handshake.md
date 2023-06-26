## **TCP (Transmission Control Protocol) 란?**

- TCP는 네트워크 계층 중 전송 계층에서 사용하는 프로토콜이다.
- TCP는 애플리케이션에게 신뢰적이고 연결지향성 서비스를 제공한다.
- TCP는 연결형 서비스로, 신뢰적인 전송을 보장하기에 hanshaking하고 데이터의 흐름제어와 혼잡제어를 수행한다.
- 하지만 이러한 기능으로 인해 TCP의 속도는 느리다.
- 인터넷상에서 데이터를 메세지의 형태로 보내기 위해 IP와 함께 사용한다.
  - IP는 배달을, TCP는 패킷의 추적 및 관리를 하게 된다.

 

## **TCP의 3 way handshake & 4 way handshake 란?**

- 연결을 성립하고 해제하는 과정을 말한다.
- 3-Way Handshake 는 TCP의 접속, 4-Way Handshake는 TCP의 접속 해제 과정이다.

 

### **TCP의 3 Way Handshake 란? (연결 성립)**

- 연결하고자 하는 두 장치 간의 논리적 접속을 성립하기 위해 사용하는 연결 확인 방식이다.
- 3번의 확인 과정 (통신)을 거친다고 해서 3 way handshake라고 부른다.



![img](https://blog.kakaocdn.net/dn/cO20Vz/btskRbobNwB/xGEXClS8NpSUNAgsImdlqK/img.png)



- TCP 통신을 이용하여 데이터를 전송하기 위해 네트워크 연결을 설정(Connection Establish) 하는 과정이다.
- 양쪽 모두 데이터를 전송할 준비가 되었다는 것을 보장하고, 실제로 데이터 전달이 시작하기 전에 한 쪽이 다른 쪽이 준비되었다는 것을 알 수 있도록 한다.
- 즉, TCP/IP 프로토콜을 이용해서 통신을 하는 응용 프로그램이 데이터를 전송하기 전에 먼저 정확한 전송을 보장하기 위해 상대방 컴퓨터와 사전에 세션을 수립하는 과정을 의미한다.

 

**TCP 3 way handshake를 간단히 표현하면 다음과 같다.**

1. A -> B : 내 말 들려?
2. B -> A : 잘 들려. 내 말은 들려?
3. A -> B : 잘 들려!

 

### **3 Way Handshake의 작동 방식**



![img](https://blog.kakaocdn.net/dn/7kdE2/btskQQklxtk/Wxk5mgU7otQDjkn3yXQrpK/img.png)



**1. Client → Server : SYN** (내 말 잘 들려?)

: 클라이언트가 서버에게 SYN 패킷을 보낸다. (sequence : x)

- 송신자가 최초로 데이터를 전송할 때 Sequence Number를 임의의 랜덤 숫자로 지정하고, SYN 플래그 비트를 1로 설정한 세그먼트를 전송한다.
- SYN (synchronize sequence numbers): 연결 확인을 위해 보내는 무작위의 숫자값

 

**2. Server → Client : SYN + ACK** (잘 들려. 내 말은 들려?)

: 서버가 SYN(x)을 받고, 클라이언트로 받았다는 신호인 ACK와 SYN 패킷을 보낸다. (sequence : y, ACK : x + 1)

- 접속요청을 받은 Q가 요청을 수락했으며, 접속 요청 프로세스인 P도 포트를 열어달라는 메세지를 전송한다. (SYN-ACK signal bits set)
- ACK Number필드를 Sequence Number + 1 로 지정하고 SYN과 ACK 플래그 비트를 1로 설정한 새그먼트 전송한다. (Seq=y, Ack=x+1, SYN, ACK)
- ACK (acknowledgements): Client 혹은 Server로부터 받은 SYN에 1을 더해 SYN을 잘 받았다는 ACK

 

**3. Client → Server : ACK** (잘 들려!)

**:** 클라이언트는 서버의 응답은 ACK(x+1)와 SYN(y) 패킷을 받고, ACK(y+1)를 서버로 보낸다.

- 마지막으로 접속 요청 프로세스 P가 수락 확인을 보내 연결을 맺는다. (ACK)
- 이때, 전송할 데이터가 있으면 이 단계에서 데이터를 전송할 수 있다.
- ISN (Initial sequence numbers): Client와 Server가 각각 처음으로 생성한 SYN

 

### **TCP의 4 way handshake 란? (연결 해제)**

- 연결 성립 후, 모든 통신이 끝났다면 해제해야 한다.
- 3 way handshake와 반대로 가상 회선 연결을 해제할 때 주고 받는 확인작업이다.
- 이 역시 4번의 확인과정(통신)을 거친다고 하여 4 way handshake라고 부른다.



![img](https://blog.kakaocdn.net/dn/Wtrs4/btskS58mF4D/jybNUVOlbNy9nSVm5Cic1k/img.png)



- 4-Way Handshake은 연결을 해제 (Connecntion Termination)하는 과정이다.

 

**TCP 4 way handshake를 간단히 표현하면 다음과 같다.**

1. A -> B: 나는 다 보냈어. 이제 끊자!
2. B -> A: 알겠어! 잠시만~
3. B -> A: 나도 끊을게!
4. A -> B: 알겠어!

 

### **4 Way Handshake 작동 방식**



![img](https://blog.kakaocdn.net/dn/VbqHR/btskRRiCukH/zNpiDoMXO6Y8vQtGev5Rq0/img.png)



**1. Client → Server : FIN(+ACK)** (나는 다 보냈어. 이제 끊자!)

: 클라이언트는 서버에게 연결을 종료한다는 FIN 플래그를 보낸다.

- 보낸 후에 FIN_WAIT_1 상태로 변한다.
- FIN 패킷에는 실질적으로 ACK도 포함되어있다.
- FIN (finish) : 세션을 종료시키는데 사용되며, 더 이상 보낸 데이터가 없음을 나타낸다.

 

**2. Server → Client : ACK** (알겠어! 잠시만~)

: 서버는 FIN을 받고, 확인했다는 ACK를 클라이언트에게 보낸다.

- 이때 모든 데이터를 보내기 위해 CLOSE_WAIT 상태가 된다.
- Client도 마찬가지로 Server에서 종료될 준비가 됐다는 FIN을 받기위해 FIN_WAIT_2 상태가 된다.

 

**3. Server → Client : FIN** (나도 끊을게!)

: 데이터를 모두 보냈다면, 연결이 종료되었다는 FIN 플래그를 클라이언트에게 보낸다.

- 클라이언트에게 보낸 후에, 승인 번호를 보내줄 때까지 기다니는 LAST_ACK 상태로 들어간다.

 

**4. Client → Server : ACK** (알겠어!)

: 클라이언트는 FIN을 받고, 확인했다는 ACK를 서버에게 보낸다.

- 단, 아직 서버로부터 받지 못한 데이터가 있을 수 있으므로 TIME_WAIT을 통해 기다린다.
- 여기서 TIME-WAIT 상태는 의도치않은 에러로 인해 연결이 데드락으로 빠지는 것을 방지하기 위해 변경 되는 것인데, 만약 에러로 인해 종료가 지연되다가 타임이 초과되면 CLOSED 상태로 변경된다.
- 서버는 ACK를 받은 이후 소켓을 닫는다. (Closed)
- TIME_WAIT 시간이 끝나면 클라이언트도 닫는다. (Closed)

------

참고 자료

https://goodgid.github.io/TCP-IP-3Way-4Way/

[https://velog.io/@averycode/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-TCPUDP%EC%99%80-3-Way-Handshake4-Way-Handshake](https://velog.io/@averycode/네트워크-TCPUDP와-3-Way-Handshake4-Way-Handshake)

https://seongonion.tistory.com/74

https://jeongkyun-it.tistory.com/180