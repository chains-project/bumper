```java
import com.jcabi.aspects.Tv;

public class AwsOcketITCase {
    public void testOcket() throws Exception {
        Tv tv = new Tv();
        tv.play("https://s3.amazonaws.com/jcabi-s3/test.mp4");
    }
}
```