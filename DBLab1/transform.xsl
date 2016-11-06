<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" version="4.0" encoding="windows-1251" indent="yes"/>
<xsl:template match="/">
  <html>
  <body>
  <h2>Products</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>ID</th>
      <th>Name</th>
      <th>Price</th>
      <th>Image</th>
    </tr>
    <xsl:for-each select="root/data/product">
    <tr>
      <td><xsl:value-of select="@id"/></td>
      <td><xsl:value-of select="name"/></td>
      <td><xsl:value-of select="price"/></td>
      <td><xsl:element name="img">
        <xsl:attribute name="src">
          <xsl:value-of select="image" />
        </xsl:attribute>
      </xsl:element></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>
