```java
  import com.jcabi.aspects.Tv;

  class AwsOcketITCase {
    public void testOcket() {
      Tv tv = new Tv();
      tv.play("https://s3.amazonaws.com/jcabi-s3/test.mp4");
    }
  }
```