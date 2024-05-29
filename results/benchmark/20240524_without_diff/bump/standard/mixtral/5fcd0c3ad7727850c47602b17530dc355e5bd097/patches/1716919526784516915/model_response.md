Here is a possible patch for the code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
In this patch, I replaced the method `getClassInfo` with the method `getClassInfoFor`, which is a new method added in the version of the library that you are using. This method takes a single argument of type `org.pitest.classinfo.ClassName` and returns the corresponding class information.

Note that this patch assumes that the library has added the method `getClassInfoFor` in a new version, and that this method behaves similarly to the old method `getClassInfo`. If this is not the case, you may need to adjust the patch accordingly.