```java
  private Matcher<String> manifestPushed() {
        boolean isDigest = this.image.digest() != null;
        String digest = isDigest ? this.image.digest() : "";
        return new StringContains(false, String.format("latest: digest: %s", digest));
    }
```