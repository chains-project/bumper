```java
  private Matcher<String> manifestPushed() {
        final String expectedDigest = String.format("latest: digest: %s", this.image.digest());
        return new StringContains(expectedDigest);
    }
```