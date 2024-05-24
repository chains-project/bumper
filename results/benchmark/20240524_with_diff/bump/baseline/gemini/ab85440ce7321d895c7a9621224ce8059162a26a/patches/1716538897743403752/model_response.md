```java
  private Matcher<String> manifestPushed() {
        String digest = this.image.digest();
        String expected = String.format("latest: digest: %s", digest);
        return new StringContains(expected);
    }
```