```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.aspects.Tv.Show;

  public class BucketRule extends Rule {

    @Override
    public void test() throws Exception {
      final Tv tv = new Tv();
      tv.play(new Show("The Wire", 1, 2));
      tv.play(new Show("The Wire", 1, 3));
      tv.play(new Show("The Wire", 1, 4));
      tv.play(new Show("The Wire", 1, 5));
      tv.play(new Show("The Wire", 1, 6));
      tv.play(new Show("The Wire", 1, 7));
      tv.play(new Show("The Wire", 1, 8));
      tv.play(new Show("The Wire", 1, 9));
      tv.play(new Show("The Wire", 1, 10));
      tv.play(new Show("The Wire", 1, 11));
      tv.play(new Show("The Wire", 1, 12));
      tv.play(new Show("The Wire", 1, 13));
      tv.play(new Show("The Wire", 2, 1));
      tv.play(new Show("The Wire", 2, 2));
      tv.play(new Show("The Wire", 2, 3));
      tv.play(new Show("The Wire", 2, 4));
      tv.play(new Show("The Wire", 2, 5));
      tv.play(new Show("The Wire", 2, 6));
      tv.play(new Show("The Wire", 2, 7));
      tv.play(new Show("The Wire", 2, 8));
      tv.play(new Show("The Wire", 2, 9));
      tv.play(new Show("The Wire", 2, 10));
      tv.play(new Show("The Wire", 2, 11));
      tv.play(new Show("The Wire", 2, 12));
      tv.play(new Show("The Wire", 2, 13));
      tv.play(new Show("The Wire", 3, 1));
      tv.play(new Show("The Wire", 3, 2));
      tv.play(new Show("The Wire", 3, 3));
      tv.play(new Show("The Wire", 3, 4));
      tv.play(new Show("The Wire", 3, 5));
      tv.play(new Show("The Wire", 3, 6));
      tv.play(new Show("The Wire", 3, 7));
      tv.play(new Show("The Wire", 3, 8));
      tv.play(new Show("The Wire", 3, 9));
      tv.play(new Show("The Wire", 3, 10));
      tv.play(new Show("The Wire", 3, 11));
      tv.play(new Show("The Wire", 3, 12));
      tv.play(new Show("The Wire", 3, 13));
      tv.play(new Show("The Wire", 4, 1));
      tv.play(new Show("The Wire", 4, 2));
      tv.play(new Show("The Wire", 4, 3));
      tv.play(new Show("The Wire", 4, 4));
      tv.play(new Show("The Wire", 4, 5));
      tv.play(new Show("The Wire", 4, 6));
      tv.play(new Show("The Wire", 4, 7));
      tv.play(new Show("The Wire", 4, 8));
      tv.play(new Show("The Wire", 4, 9));
      tv.play(new Show("The Wire", 4, 10));
      tv.play(new Show("The Wire", 4, 11));
      tv.play(new Show("The Wire", 4, 12));
      tv.play(new Show("The Wire", 4, 13));
      tv.play(new Show("The Wire", 5, 1));
      tv.play(new Show("The Wire", 5, 2));
      tv.play(new Show("The Wire", 5, 3));
      tv.play(new Show("The Wire", 5, 4));
      tv.play(new Show("The Wire", 5, 5));
      tv.play(new Show("The Wire", 5, 6));
      tv.play(new Show("The Wire", 5, 7));
      tv.play(new Show("The Wire", 5, 8));
      tv.play(new Show("The Wire", 5, 9));
      tv.play(new Show("The Wire", 5, 10));
      tv.play(new Show("The Wire", 5, 11));
      tv.play(new Show("The Wire", 5, 12));
      tv.play(new Show("The Wire", 5, 13));
    }

  }
```