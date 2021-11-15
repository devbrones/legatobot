
                if a_.agenda.find(substring) != -1:
                    urel = str(str(a_.url).replace("['", "").replace("']", "")
                    await buttons.send(content = None, embed = embedVar, channel = ctx.channel.id, components=[ActionRow([Button(label = "Hperlink", style = ButtonType().Link, url = urel])])
                else:
                    print("NULL_HYPERLINK_AGENDA")
                    await ctx.send(embed=embedVar)
