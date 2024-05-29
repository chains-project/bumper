Here's a possible patch for the given client code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
The change is to replace the method `getClassInfo` with `getClassInfoFor`, which is an added library method identified with `++`. This should solve the error message regarding the missing symbol for `getClassInfo`.