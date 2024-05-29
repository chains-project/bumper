Here is a potential patch for the client code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
This patch uses the `getClassInfoFor` method of the `CoverageDatabase` class instead of `getClassInfo`, which should resolve the "cannot find symbol" error. This method was added in a later version of the library, so it may not be available in earlier versions.