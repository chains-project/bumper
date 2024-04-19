```java
  private Matcher<String> manifestPushed() {
        String digest = this.image.digest();
        return new StringContains(false, String.format("latest: digest: %s", digest));
    }
```