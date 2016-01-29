
#define trigPin 8
#define echoPin 12
#define led 13

void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(led, OUTPUT);

}

void clear(){
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
}

void loop() {
  long duration, distance;
  clear();
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1; //from their site
  if (distance < 20) {  
    digitalWrite(led,HIGH); 

}
  else {
    digitalWrite(led,LOW);

  }
  delay(500);
}
