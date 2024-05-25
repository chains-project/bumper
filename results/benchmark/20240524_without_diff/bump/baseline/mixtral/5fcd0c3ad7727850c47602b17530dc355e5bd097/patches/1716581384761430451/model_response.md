Sure, here is a proposed patch for the failing client code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```
In this patch, I have created a new variable `classInfo` to store the result of `coverage.getClassInfo(Collections.singleton(data.getMutatedClass()))`. This way, the code is easier to read and understand. Also, it avoids calling the library method twice, which might have been causing the error.

Note that I did not use any removed library methods (`--`) or added library methods (`++`). I only changed the way the code is written to make it more readable and avoid potential errors.