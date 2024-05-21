Here is the proposed patch:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

I changed the `getClassInfo` method to `getClassInfoFor`, which is an added library method identified with `++`. This should fix the error caused by the missing `getClassInfo` method.