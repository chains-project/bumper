```java
  private Matcher<String> manifestPushed() {
        String digest = this.image.digest();
        String expected = "latest: digest: " + digest;
        return new StringContains(false, expected);
    }
```