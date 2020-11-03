import discord
from discord.ext import commands

class MemberRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    # For kick, ban it will be more specific in the log this is just a global event for kick ban etc
    async def on_member_remove(self, member):
        logch = self.bot.db.execute('')
        if logch:
            moderator = None
            action = None
            reason = None
        if member.guild.me.guild_permissions.view_audit_log:
            async for e in member.guild.audit_logs(limit=5):
                if e.action in [discord.AuditLogAction.kick, discord.AuditLogAction.ban] and e.target.id == member.id:
                    moderator = e.user
                    if moderator == member.guild.me:
                        moderator = None
                        break
                if e.action == discord.AuditLogAction.kick:
                    action = 'kick'
                    reason = e.reason
                



def setup(bot):
    bot.add_cog(MemberRemove(bot))