Here is a possible patch for the given code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
In this patch, I replaced the method `getClassInfo` with `getClassInfoFor`, which is a new method added in the version of the library that you're using. This method takes a single `ClassName` argument instead of a `Set<ClassName>`. I also changed the argument of `getClassInfoFor` method to `data.getMutatedClass()`, as it is an instance of `ClassName`.