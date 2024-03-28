```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.log.Logger;
  import com.jcabi.log.LoggerFactory;

  class AwsOcketITCase {

    private static final Logger LOG = LoggerFactory.getLogger(AwsOcketITCase.class);

    @Tv
    void testWith() {
      LOG.info("Testing with");
    }
  }
```