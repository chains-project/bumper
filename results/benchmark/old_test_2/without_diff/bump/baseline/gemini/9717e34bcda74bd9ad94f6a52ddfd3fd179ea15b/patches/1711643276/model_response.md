```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.github.mock.MkGithub;

  class MyGithub extends MkGithub {

    @Override
    public Tv tv() {
      return null;
    }
  }
```