```java
import com.jcabi.aspects.Tv;

import java.util.Arrays;
import java.util.List;

public class AwsOcketITCase {

  public static void main(String[] args) {
    List<Tv> tvs = Arrays.asList(
        new Tv("Samsung", 2023, 1000),
        new Tv("LG", 2022, 1500),
        new Tv("Sony", 2021, 2000)
    );

    tvs.stream()
        .filter(tv -> tv.getYear() >= 2022)
        .forEach(tv -> System.out.println(tv.getName() + " " + tv.getPrice()));
  }
}
```