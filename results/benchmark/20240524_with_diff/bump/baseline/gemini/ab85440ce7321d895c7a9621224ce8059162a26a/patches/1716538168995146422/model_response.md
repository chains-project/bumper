```java
  private Matcher<String> manifestPushed() {
        boolean isLatest = "latest".equals(this.image.tag());
        String digest = isLatest ? "" : String.format(" digest: %s", this.image.digest());
        return new StringContains(false, String.format("latest:%s", digest));
    }
```