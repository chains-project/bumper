```java
import com.jcabi.aspects.Tv;
import com.jcabi.aspects.TvProxy;

import java.lang.reflect.Proxy;

public class AwsOcketITCase {

    private final Tv tv = (Tv) Proxy.newProxyInstance(
            AwsOcketITCase.class.getClassLoader(),
            new Class<?>[]{Tv.class},
            new TvProxy(new MyTv())
    );

    public void testWithTv() throws Exception {
        tv.play("123");
    }

    private static class MyTv implements Tv {
        @Override
        public void play(String id) {
            // do nothing
        }
    }
}
```