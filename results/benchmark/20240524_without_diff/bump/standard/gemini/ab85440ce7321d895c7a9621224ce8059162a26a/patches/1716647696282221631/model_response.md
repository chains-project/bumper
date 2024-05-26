```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return new org.hamcrest.core.SubstringMatcher(java.lang.String.format("%s: Pushed", this.image.layer())) {
        @Override
        protected boolean evalSubstringOf(String s) {
            return !s.contains(this.substring);
        }

        @Override
        protected String relationship() {
            return "not containing";
        }
    };
}
```